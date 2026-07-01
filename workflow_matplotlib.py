"""
mutator_workflow.py

Endpoint-preserving path-mutation tester (SR / RS / RR) with
ValueError-driven recovery.

If a Set-Revert mutation triggers a ValueError such as
    "'x' is not a valid value for align; supported values are
     'top', 'bottom', 'center', 'baseline', 'center_baseline'"
the workflow:
  (a) parses the listed supported values, picks one != current,
      and retries the same Set-Revert with that value;
  (b) if no supported set can be parsed, falls back to Redundant-Set
      on the same (get_x, set_x) pair.
"""

import io, os, sys, json, random, argparse, datetime, textwrap, traceback
import subprocess, re
from typing import Any, List, Tuple, Optional, Callable

import imagehash
import numpy as np
from PIL import Image
from tqdm import tqdm

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from utils_matplotlib import (
    Node, get_tree, sample_node, sample_removable_node, format_access_path
)

# ============================================================
# Constants
# ============================================================
DEFAULT_K          = 5
DEFAULT_THRESHOLD  = 3
P_REMOVE_READD    = 0.15
P_REDUNDANT_SET   = 0.20

_EXCLUDED_GETTERS = {
    "get_bbox_to_anchor", "get_constrained_layout", "get_layout_engine",
    "get_ticklabels", "get_tight_layout", "get_transform",
    "get_xmargin", "get_ymargin", "get_xticklabels", "get_yticklabels",
    "get_figure",
}

# ============================================================
# Generic utilities
# ============================================================

def find_test_scripts(seed_dir: str) -> List[str]:
    out = []
    for d, _, fs in os.walk(seed_dir):
        for fn in fs:
            if fn.startswith("seed_") and fn.endswith(".py"):
                out.append(os.path.join(d, fn))
    return out

def ensure_dir(p: str) -> None:
    os.makedirs(p, exist_ok=True)

def safe_slug(s: str, n: int = 120) -> str:
    out = "".join(c if (c.isalnum() or c in "-_.") else "_" for c in s)
    while "__" in out:
        out = out.replace("__", "_")
    return out[:n].strip("_") or "case"

def render_fig_rgba(fig) -> Image.Image:
    buf = io.BytesIO(); fig.savefig(buf); buf.seek(0)
    buf = io.BytesIO(); fig.savefig(buf); buf.seek(0)
    return Image.open(buf).convert("RGBA")

def phash_distance(a: Image.Image, b: Image.Image) -> int:
    return imagehash.phash(a) - imagehash.phash(b)

# ============================================================
# Property introspection
# ============================================================

def paired_get_set_methods(elem) -> List[Tuple[str, str]]:
    try:
        getters = {
            m for m in dir(elem)
            if m.startswith("get_") and callable(getattr(elem, m, None))
            and m not in _EXCLUDED_GETTERS
        }
        pairs = []
        for m in dir(elem):
            if m.startswith("set_") and callable(getattr(elem, m, None)):
                g = "get_" + m[4:]
                if g in getters:
                    pairs.append((g, m))
        return pairs
    except Exception:
        return []

def is_removable(elem) -> bool:
    return getattr(elem, "_remove_method", None) is not None

# ============================================================
# Value selection
# ============================================================

def _parse_doc_enum(setter) -> List[str]:
    doc = setter.__doc__ or ""
    try:
        i = doc.find("Parameters")
        i = doc.find("----------", i)
        i = doc.find(" : ", i) + 3
        m = re.search(r"\{([^}]*)\}", doc[i:])
        if m:
            return re.findall(r"'([^']*)'", m.group(1))
    except Exception:
        pass
    return []

def select_mutation_value(elem, get_m: str, set_m: str) -> Tuple[bool, Any]:
    try:
        cur = getattr(elem, get_m)()
    except Exception:
        return False, None

    enum_vals = _parse_doc_enum(getattr(elem, set_m))
    if enum_vals:
        cands = [v for v in enum_vals if v != cur]
        if cands:
            return True, random.choice(cands)

    if isinstance(cur, bool):
        return True, (not cur)

    if isinstance(cur, (int, np.integer)) and not isinstance(cur, bool):
        cur_i = int(cur)
        pool = [0, 1, -1, cur_i + 1, cur_i - 1, cur_i * 2, cur_i + 1000]
        cands = [v for v in pool if v != cur_i]
        return (True, random.choice(cands)) if cands else (False, None)

    if isinstance(cur, (float, np.floating)):
        cur_f = float(cur)
        pool = [0.0, 1.0, -1.0, cur_f + 1.0, cur_f - 1.0,
                cur_f * 2.0, cur_f + 1e-9, cur_f - 1e-9]
        cands = [v for v in pool if v != cur_f and not np.isnan(v)]
        return (True, random.choice(cands)) if cands else (False, None)

    if isinstance(cur, str):
        pool = ["", " ", "x", "Sample", "0", "AB"]
        cands = [v for v in pool if v != cur]
        return (True, random.choice(cands)) if cands else (False, None)

    if isinstance(cur, matplotlib.text.Text):
        return True, "X"

    return False, None

# ============================================================
# Operator code-generation primitives
# ============================================================

def _build_sr_with_value(access_expr: str, elem,
                        get_m: str, set_m: str, v_prime: Any
                        ) -> Tuple[str, Callable, tuple]:
    v_repr = repr(v_prime)
    snippet = textwrap.dedent(f"""\
        _e = {access_expr}
        _v = _e.{get_m}()
        _e.{set_m}({v_repr})
        _e.{set_m}(_v)""")

    def _apply(_e=elem, _g=get_m, _s=set_m, _vp=v_prime):
        v = getattr(_e, _g)()
        getattr(_e, _s)(_vp)
        getattr(_e, _s)(v)

    return snippet, _apply, ("SR", set_m, v_prime)

def _build_rs(access_expr: str, elem,
              get_m: str, set_m: str
              ) -> Tuple[str, Callable, tuple]:
    snippet = textwrap.dedent(f"""\
        _e = {access_expr}
        _v = _e.{get_m}()
        _e.{set_m}(_v)""")

    def _apply(_e=elem, _g=get_m, _s=set_m):
        getattr(_e, _s)(getattr(_e, _g)())

    return snippet, _apply, ("RS", set_m, None)

# ============================================================
# Operator dispatch (Section 3.4)
# ============================================================

def gen_set_revert(access_expr: str, elem) -> Optional[Tuple[str, Callable, tuple]]:
    pairs = paired_get_set_methods(elem)
    if not pairs:
        return None
    random.shuffle(pairs)
    for get_m, set_m in pairs:
        ok, v_prime = select_mutation_value(elem, get_m, set_m)
        if not ok:
            continue
        try:
            eval(repr(v_prime), {"__builtins__": {}})
        except Exception:
            continue
        return _build_sr_with_value(access_expr, elem, get_m, set_m, v_prime)
    return None

def gen_redundant_set(access_expr: str, elem) -> Optional[Tuple[str, Callable, tuple]]:
    pairs = paired_get_set_methods(elem)
    if not pairs:
        return None
    get_m, set_m = random.choice(pairs)
    return _build_rs(access_expr, elem, get_m, set_m)

def gen_remove_readd(access_expr: str, elem) -> Optional[Tuple[str, Callable, tuple]]:
    if not is_removable(elem):
        return None

    snippet = textwrap.dedent(f"""\
        _e = {access_expr}
        _parent = _e.axes if getattr(_e, 'axes', None) is not None else _e.figure
        _e.remove()
        _parent.add_artist(_e)""")

    def _apply(_e=elem):
        parent = getattr(_e, "axes", None) or getattr(_e, "figure", None)
        if parent is None:
            raise RuntimeError("no parent for remove-readd")
        _e.remove()
        parent.add_artist(_e)

    return snippet, _apply, ("RR", "remove_readd", None)

def gen_mutation(access_expr: str, elem) -> Optional[Tuple[str, Callable, tuple]]:
    r = random.random()
    if r < P_REMOVE_READD and is_removable(elem):
        order = [gen_remove_readd, gen_set_revert, gen_redundant_set]
    elif r < P_REMOVE_READD + P_REDUNDANT_SET:
        order = [gen_redundant_set, gen_set_revert, gen_remove_readd]
    else:
        order = [gen_set_revert, gen_redundant_set, gen_remove_readd]

    for fn in order:
        out = fn(access_expr, elem)
        if out is not None:
            return out
    return None

# ============================================================
# ValueError-driven recovery
# ============================================================

# Matches "supported values are 'a', 'b', "c", ..." — case-insensitive,
# tolerant of trailing periods / newlines.
_SUPPORTED_RE = re.compile(
    r"supported values are\s+(.+)$",
    re.IGNORECASE | re.DOTALL,
)

def _parse_supported_values(err_msg: str) -> List[str]:
    """
    Extract the quoted token list following 'supported values are ...'.
    Returns [] if the pattern is absent.
    """
    m = _SUPPORTED_RE.search(err_msg)
    if not m:
        return []
    tail = m.group(1)
    # Stop at end-of-sentence markers if present.
    cut = re.search(r"[\n\r]", tail)
    if cut:
        tail = tail[:cut.start()]
    tokens = re.findall(r"['\"]([^'\"]+)['\"]", tail)
    return tokens

def _try_apply_with_recovery(
    apply_fn: Callable,
    snippet: str,
    meta: tuple,
    elem,
    access_expr: str,
    verbose: bool = False,
) -> Tuple[bool, str, Callable, tuple, Optional[str]]:
    """
    Attempt apply_fn(); if it raises ValueError on a Set-Revert mutation,
    try to recover by:
      (a) parsing 'supported values are ...' from the message and retrying
          Set-Revert with one of those values, or
      (b) falling back to Redundant-Set on the same getter/setter pair.

    Returns (ok, snippet, apply_fn, meta, last_error_msg).

    NOTE: ValueError is *never* treated as a bug — it usually reflects a
    value-format mismatch between get_*() and set_*() (e.g. the getter
    returns a normalized form the setter does not accept). When recovery
    fails, ok=False is returned and the caller is expected to skip this
    round silently rather than emit a bug report.
    """
    try:
        apply_fn()
        return True, snippet, apply_fn, meta, None
    except ValueError as ve:
        if meta[0] != "SR":
            # RS / RR ValueError: also treat as value-format issue, skip.
            return False, snippet, apply_fn, meta, str(ve)

        set_m = meta[1]
        get_m = "get_" + set_m[4:]
        try:
            cur = getattr(elem, get_m)()
        except Exception:
            cur = object()

        supported = _parse_supported_values(str(ve))
        alts = [v for v in supported if v != cur]

        if alts:
            v_new = random.choice(alts)
            if verbose:
                print(f"           [recover] SR -> SR with v'={v_new!r} "
                      f"(parsed {len(supported)} supported values)")
            new_snip, new_apply, new_meta = _build_sr_with_value(
                access_expr, elem, get_m, set_m, v_new
            )
            try:
                new_apply()
                return True, new_snip, new_apply, new_meta, None
            except ValueError as e2:
                if verbose:
                    print(f"           [recover] retried SR ValueError: {e2}; "
                          f"falling back to RS")
            except Exception as e2:
                if verbose:
                    print(f"           [recover] retried SR failed: {e2}; "
                          f"falling back to RS")

        # (b) Fall back to Redundant-Set on the same (get_x, set_x).
        if verbose:
            print(f"           [recover] SR -> RS on ({get_m}, {set_m})")
        rs_snip, rs_apply, rs_meta = _build_rs(access_expr, elem, get_m, set_m)
        try:
            rs_apply()
            return True, rs_snip, rs_apply, rs_meta, None
        except ValueError as e3:
            # RS itself ValueErrors -> still a value-format issue, skip.
            return False, rs_snip, rs_apply, rs_meta, str(e3)
        except Exception as e3:
            # Non-ValueError on RS: still don't escalate here; let the
            # main loop's render-time check decide. Skip silently.
            return False, rs_snip, rs_apply, rs_meta, str(e3)

# ============================================================
# BRT script construction
# ============================================================

def build_brt_script(original_src: str,
                     snippets: List[str],
                     threshold: int) -> str:
    src = original_src.replace("plt.show()", "")

    header = textwrap.dedent(f"""\
        # ============================================================
        # BRT (Bug Repro Test) script auto-generated by mutator_workflow.
        # phash threshold (tau) = {threshold}
        # ============================================================

        import io, imagehash
        from PIL import Image
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt

        def _brt_render(_fig):
            _buf = io.BytesIO(); _fig.savefig(_buf); _buf.seek(0)
            _buf = io.BytesIO(); _fig.savefig(_buf); _buf.seek(0)
            return Image.open(_buf).convert("RGBA")

        _fig = plt.gcf()
        _ref = _brt_render(_fig)
        """)

    body = "\n".join(f"# --- Delta_{i+1} ---\n{sn}"
                     for i, sn in enumerate(snippets))

    footer = textwrap.dedent(f"""\

        _post = _brt_render(_fig)
        _d = imagehash.phash(_ref) - imagehash.phash(_post)
        assert _d < {threshold}, (
            f"Endpoint-preserving mutation altered rendering "
            f"(phash distance = {{_d}} >= {threshold})"
        )
        """)

    return src + "\n\n" + header + body + "\n" + footer

# ============================================================
# Workflow (Algorithm 1)
# ============================================================

def run_workflow_on_script(
    script_path: str,
    K: int = DEFAULT_K,
    threshold: int = DEFAULT_THRESHOLD,
    export_dir: Optional[str] = None,
    verbose: bool = False,
) -> Tuple[bool, List[dict]]:

    plt.close("all")

    with open(script_path) as f:
        original_src = f.read()
    src = original_src.replace("plt.show()", "")

    ns: dict = {}
    try:
        exec(src, ns, ns)
        fig = plt.gcf()
        if fig is None:
            raise RuntimeError("seed produced no figure")
        ref_img = render_fig_rgba(fig)
    except Exception as e:
        return False, [{
            "kind": "exec", "script_path": script_path,
            "message": str(e), "traceback": traceback.format_exc(),
        }]

    snippets: List[str] = []
    metas: List[tuple] = []

    for k in range(K):
        try:
            root = get_tree(fig)
        except Exception as e:
            return False, [{
                "kind": "build_tree", "round": k, "script_path": script_path,
                "message": str(e), "traceback": traceback.format_exc(),
            }]

        if getattr(root, "size", 0) == 0:
            break

        try:
            sample = sample_node(root)
        except Exception as e:
            if verbose: print(f"  round {k}: sample failed: {e}")
            continue
        elem = getattr(sample, "e", None)
        if elem is None:
            continue
        try:
            access_expr = format_access_path("plt.gcf()", sample)
        except Exception:
            continue

        mut = gen_mutation(access_expr, elem)
        if mut is None:
            if verbose:
                print(f"  round {k}: no applicable operator on "
                      f"{type(elem).__name__}")
            continue
        snippet, apply_fn, meta = mut

        if verbose:
            print(f"  round {k}: op={meta[0]} elem={type(elem).__name__} "
                  f"prop={meta[1]} val={meta[2]!r}")

        # Apply with ValueError-driven recovery.
        ok, snippet, apply_fn, meta, err_msg = _try_apply_with_recovery(
            apply_fn, snippet, meta, elem, access_expr, verbose=verbose
        )

        if not ok:
            # ValueError (or recovery-stage failure) is treated as a
            # value-format mismatch between get_*() and set_*(), NOT a bug.
            # Drop this round's Delta and move on.
            if verbose:
                print(f"           [skip] round {k}: value-format issue "
                      f"({meta[0]} {meta[1]}): {err_msg}")
            continue

        snippets.append(snippet)
        metas.append(meta)

        try:
            cur_img = render_fig_rgba(fig)
        except Exception as e:
            brt_path = _emit_brt(export_dir, script_path, original_src,
                                 snippets, metas, threshold, suffix="rendercrash")
            return False, [{
                "kind": "render_crash",
                "round": k, "operator": meta[0],
                "access_expr": access_expr,
                "method": meta[1], "value": repr(meta[2]),
                "message": str(e),
                "traceback": traceback.format_exc(),
                "brt_path": brt_path,
            }]

        d = phash_distance(ref_img, cur_img)
        if verbose:
            print(f"           phash distance = {d}")

        if d >= threshold:
            brt_path = _emit_brt(export_dir, script_path, original_src,
                                 snippets, metas, threshold, suffix="oracle")
            return False, [{
                "kind": "oracle_mismatch",
                "round": k, "operator": meta[0],
                "access_expr": access_expr,
                "method": meta[1], "value": repr(meta[2]),
                "phash_distance": int(d),
                "brt_path": brt_path,
            }]

    return True, []


def _emit_brt(export_dir, script_path, original_src,
              snippets, metas, threshold, suffix) -> Optional[str]:
    if not export_dir:
        return None
    ensure_dir(export_dir)
    base = os.path.splitext(os.path.basename(script_path))[0]
    op_tag = "_".join(f"{m[0]}-{m[1]}" for m in metas[-3:])
    name = safe_slug(f"{base}__{suffix}__{op_tag}")
    path = os.path.join(export_dir, f"{name}.py")
    with open(path, "w", encoding="utf-8") as f:
        f.write(build_brt_script(original_src, snippets, threshold))
    return path

# ============================================================
# JSON encoder
# ============================================================

class _SafeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):  return int(obj)
        if isinstance(obj, np.floating):
            return repr(obj) if (np.isnan(obj) or np.isinf(obj)) else float(obj)
        if isinstance(obj, np.ndarray):  return obj.tolist()
        if isinstance(obj, bytes):       return obj.decode("utf-8", "replace")
        try: return super().default(obj)
        except TypeError: return repr(obj)

# ============================================================
# Worker / orchestrator
# ============================================================

def _worker_mode(args: argparse.Namespace) -> None:
    random.seed(args.worker_seed)
    success, errors = run_workflow_on_script(
        script_path  = args.worker_script,
        K            = args.K,
        threshold    = args.threshold,
        export_dir   = args.worker_export_dir,
        verbose      = False,
    )
    sys.stdout.write(json.dumps(
        {"success": success, "errors": errors}, cls=_SafeEncoder
    ))
    sys.stdout.flush()

def run_script_in_subprocess(script_path, K, threshold, seed,
                             export_dir, timeout=120, verbose=True):
    cmd = [
        sys.executable, __file__, "--worker",
        "--worker-script", script_path,
        "--worker-seed", str(seed),
        "--K", str(K),
        "--threshold", str(threshold),
    ]
    if export_dir:
        cmd += ["--worker-export-dir", export_dir]

    try:
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE, text=True)
        stdout, stderr = proc.communicate(timeout=timeout)
    except subprocess.TimeoutExpired:
        proc.kill(); proc.communicate()
        if verbose: print(f"[timeout] {script_path}")
        return
    except Exception as e:
        if verbose: print(f"[error] {e}")
        return

    if proc.returncode != 0 and not stdout.strip():
        if verbose:
            print(f"[crash] {script_path} (exit {proc.returncode})")
            if stderr: print("  stderr:", stderr[:1500])
        return

    if verbose:
        print(f"[done] {script_path}: {stdout.strip()[:200]}")

# ============================================================
# CLI
# ============================================================

def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Endpoint-preserving path-mutation tester (SR/RS/RR)."
    )
    p.add_argument("--seed_dir", default="seeds/matplotlib")
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--K", type=int, default=DEFAULT_K)
    p.add_argument("--threshold", type=int, default=DEFAULT_THRESHOLD)
    p.add_argument("--timeout", type=int, default=120)
    p.add_argument("--worker", action="store_true", help=argparse.SUPPRESS)
    p.add_argument("--worker-script", dest="worker_script",
                   default=None, help=argparse.SUPPRESS)
    p.add_argument("--worker-seed", dest="worker_seed",
                   type=int, default=0, help=argparse.SUPPRESS)
    p.add_argument("--worker-export-dir", dest="worker_export_dir",
                   default=None, help=argparse.SUPPRESS)
    return p

if __name__ == "__main__":
    args = _build_parser().parse_args()

    if args.worker:
        _worker_mode(args); sys.exit(0)

    random.seed(args.seed)
    test_scripts = find_test_scripts(args.seed_dir)
    print(f"Found {len(test_scripts)} seed scripts in {args.seed_dir}.")
    print(f"K={args.K}  tau={args.threshold}  timeout={args.timeout}s")

    run_ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    run_dir = os.path.join("brt_workflow_matplotlib", run_ts)
    ensure_dir(run_dir)
    print(f"Export directory: {run_dir}\n")

    total = 0
    while True:
        sp = random.choice(test_scripts)
        export_dir = os.path.join(run_dir, safe_slug(
            os.path.splitext(os.path.basename(sp))[0]
        ))
        ensure_dir(export_dir)
        run_script_in_subprocess(
            script_path = sp,
            K           = args.K,
            threshold   = args.threshold,
            seed        = random.randint(0, 2**31 - 1),
            export_dir  = export_dir,
            timeout     = args.timeout,
            verbose     = False,
        )
        total += 1
        if total % 100 == 0:
            print(f"[{datetime.datetime.now():%Y-%m-%d %H:%M:%S}] "
                  f"iterations: {total}")
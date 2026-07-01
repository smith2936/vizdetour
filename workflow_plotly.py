import argparse, time, io, os, json, re, math, random, sys, subprocess, imagehash
import multiprocessing as mp
from datetime import datetime

import numpy as np
import plotly.io as pio
from playwright.sync_api import sync_playwright
from PIL import Image

from utils_plotly import extractCandidates, ElementTree

# ---------------------------------------------------------------------------
# Custom exception — carries mutation context so the catch-site can act on it
# (Plotly analogue of Bokeh's MutationRenderError)
# ---------------------------------------------------------------------------

class MutationRenderError(AssertionError):
    """Raised when a no-op mutation produces a visible rendering difference."""

    def __init__(self, message, path, prop, original_value, mutated_value):
        super().__init__(message)
        self.path = path                      # e.g. "fig.data[0].marker"
        self.prop = prop                      # e.g. "colorscale"
        self.original_value = original_value
        self.mutated_value = mutated_value
        # Attached after construction (same process — no pickling needed):
        self.img1 = None                      # Python-side mutation screenshot
        self.img2 = None                      # JS-side restyle/relayout screenshot


# ---------------------------------------------------------------------------
# Core helpers
# ---------------------------------------------------------------------------

def safe_value_repr(value) -> str:
    """Return a string that is a valid Python *expression* for *value*.

    Normalises numpy scalars/arrays to native Python and turns the special
    floats into valid literals (``repr(float('inf'))`` -> ``'inf'`` is NOT
    a valid Python literal).
    """
    if isinstance(value, np.generic):
        value = value.item()
    if isinstance(value, np.ndarray):
        value = value.tolist()
    if isinstance(value, float):
        if math.isnan(value):
            return "float('nan')"
        if math.isinf(value):
            return "float('inf')" if value > 0 else "float('-inf')"
    return repr(value)


def js_value(v) -> str:
    """JSON for Plotly.js; None -> null (i.e. property removal)."""
    if isinstance(v, np.generic):
        v = v.item()
    elif isinstance(v, np.ndarray):
        v = v.tolist()
    return json.dumps(v)


def images_similar(img1, img2, threshold: int = 3) -> bool:
    return imagehash.phash(img1) - imagehash.phash(img2) < threshold


def get_time_str() -> str:
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def prepare_seed(raw: str) -> str:
    """Apply the same seed transforms the prototype uses:

    - drop the JSON renderer call
    - pin random / numpy seeds so the figure is deterministic
    """
    raw = raw.replace('fig.show(renderer="json")', '')
    return ("import random; random.seed(42)\n"
            "import numpy as np; np.random.seed(42)\n" + raw)


def get_seeds(seed_dir: str):
    """Yield seed scripts that actually build a ``fig`` object."""
    for file in os.listdir(seed_dir):
        if not file.endswith(".py"):
            continue
        path = os.path.join(seed_dir, file)
        with open(path) as f:
            code = f.read()
        if "fig" in code:
            yield path
        else:
            print(f"Skipping {path}: no 'fig' object found")


# ---------------------------------------------------------------------------
# JS injection — build the restyle / relayout trigger
#   Simplify to minimal form: data path -> Plotly.restyle, layout path -> relayout
# ---------------------------------------------------------------------------

def build_js_call(full_path: str, mutated_value) -> str:
    """Return the single ``Plotly.restyle(...)`` / ``Plotly.relayout(...)`` call."""
    mdata = re.match(r"fig\.data\[(\d+)\]\.(.+)", full_path)
    if mdata:                                                  # --- restyle path ---
        trace_idx = int(mdata.group(1))
        attr      = mdata.group(2)                             # "marker.colorscale"
        return (f"Plotly.restyle(plotEl, "
                f"{{{json.dumps(attr)}: {js_value(mutated_value)}}}, "
                f"[{trace_idx}])")
    # --- relayout path ---
    attr = re.match(r"fig\.layout\.(.+)", full_path).group(1)  # "yaxis.autorange"
    return (f"Plotly.relayout(plotEl, "
            f"{{{json.dumps(attr)}: {js_value(mutated_value)}}})")


def build_js_trigger(full_path: str, mutated_value) -> str:
    js_call = build_js_call(full_path, mutated_value)
    return f"""
<script>
    window.addEventListener('DOMContentLoaded', (event) => {{
        var plotEl = document.getElementsByClassName('plotly-graph-div')[0];
        setTimeout(function() {{
            // No console.log in headless: it perturbs timing/rendering!
            {js_call};
        }}, 1000);
    }});
</script>
"""


# ---------------------------------------------------------------------------
# Playwright capture — two HTML strings -> two PIL images (in-memory)
# ---------------------------------------------------------------------------

def capture_screenshots(html_content_1: str, html_content_2: str):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1200, "height": 800})
        page = context.new_page()

        page.set_content(html_content_1)        # Native control group
        time.sleep(1.5)
        img_bytes_1 = page.screenshot()

        page.set_content(html_content_2)        # Restyled experimental group
        time.sleep(2.0)
        img_bytes_2 = page.screenshot()

        browser.close()

    img1 = Image.open(io.BytesIO(img_bytes_1))
    img2 = Image.open(io.BytesIO(img_bytes_2))
    return img1, img2


# ---------------------------------------------------------------------------
# Mutation — sample element, pick a primitive prop, mutate, compare
# ---------------------------------------------------------------------------

def mutate_fig(fig, threshold: int) -> None:
    """Mutate one property of a stratified-sampled element; raise on divergence."""
    process_name = mp.current_process().name

    tree = ElementTree(fig)
    elem, path = tree.sample_stratified()
    print(f"[{process_name}] Sampled element path: {path}")
    assert eval(path, {"fig": fig}) is elem    # path resolves to the same object

    # fig root has no _valid_props — only data/layout sub-elements do.
    if not hasattr(elem, "_valid_props"):
        print(f"[{process_name}] {path} has no _valid_props — skipping")
        return

    props = list(elem._valid_props)
    if not props:
        print(f"[{process_name}] {path} exposes no props — skipping")
        return

    # Try up to 5 times to land on a property whose current value is primitive
    # (i.e. a leaf, not a nested compound like 'marker').
    prop = random.choice(props)
    for _ in range(5):
        prop = random.choice(props)
        if not hasattr(getattr(elem, prop), "_valid_props"):
            break

    validator = elem._get_validator(prop)
    original_value = getattr(elem, prop)

    candidates = extractCandidates(validator)
    candidates.append(original_value)
    candidates.append(None)                    # None -> removal
    mutated_value = random.choice(candidates)

    full_path = f"{path}.{prop}"               # e.g. "fig.data[0].marker.colorscale"
    print(f"[{process_name}] {full_path}: {original_value!r} -> {mutated_value!r}")

    # --- Case 1: Python-side mutation BEFORE render ---
    setattr(elem, prop, mutated_value)
    html_content_1 = pio.to_html(fig, full_html=True, include_plotlyjs='cdn')
    setattr(elem, prop, original_value)        # restore for clean Case 2

    # --- Case 2: render first, then mutate via injected JS AFTER load ---
    html_content_2 = pio.to_html(fig, full_html=True, include_plotlyjs='cdn')
    js_trigger = build_js_trigger(full_path, mutated_value)
    html_content_2 = html_content_2.replace("</body>", f"{js_trigger}\n</body>")

    img1, img2 = capture_screenshots(html_content_1, html_content_2)

    distance = imagehash.phash(img1) - imagehash.phash(img2)
    print(f"[{process_name}] pHash distance: {distance}")

    if not images_similar(img1, img2, threshold):
        err = MutationRenderError(
            f"No-op mutation diverged: setting {full_path} to {mutated_value!r} "
            f"(Python-before-render) vs JS-after-render differ (dist={distance})",
            path=path,
            prop=prop,
            original_value=original_value,
            mutated_value=mutated_value,
        )
        err.img1 = img1
        err.img2 = img2
        raise err


# ---------------------------------------------------------------------------
# Bug-reproducer writer
# ---------------------------------------------------------------------------

# Body is a raw triple-SINGLE-quoted constant so its inner triple-DOUBLE-quoted
# JS template and regex backslashes survive verbatim (no f-string brace games).
_REPRODUCER_BODY = r'''
# ── Reproducer driver ─────────────────────────────────────────────────────────
import io, re, json, time
import imagehash
import numpy as np
import plotly.io as pio
from PIL import Image
from playwright.sync_api import sync_playwright

elem = eval(_PATH, {"fig": fig})
full_path = _PATH + "." + _PROP


def _js_value(v):
    if isinstance(v, np.generic):
        v = v.item()
    elif isinstance(v, np.ndarray):
        v = v.tolist()
    return json.dumps(v)


# ── Case 1: Python-side mutation applied BEFORE rendering ─────────────────────
setattr(elem, _PROP, _MUTATED)
html_content_1 = pio.to_html(fig, full_html=True, include_plotlyjs="cdn")
setattr(elem, _PROP, _ORIGINAL)              # restore for a clean Case 2

# ── Case 2: render first, then mutate via injected JS AFTER load ─────────────
html_content_2 = pio.to_html(fig, full_html=True, include_plotlyjs="cdn")

mdata = re.match(r"fig\.data\[(\d+)\]\.(.+)", full_path)
if mdata:
    trace_idx = int(mdata.group(1))
    attr      = mdata.group(2)
    js_call = ("Plotly.restyle(plotEl, {" + json.dumps(attr) + ": "
               + _js_value(_MUTATED) + "}, [" + str(trace_idx) + "])")
else:
    attr = re.match(r"fig\.layout\.(.+)", full_path).group(1)
    js_call = ("Plotly.relayout(plotEl, {" + json.dumps(attr) + ": "
               + _js_value(_MUTATED) + "})")

js_trigger = """
<script>
    window.addEventListener('DOMContentLoaded', (event) => {
        var plotEl = document.getElementsByClassName('plotly-graph-div')[0];
        setTimeout(function() {
            __JSCALL__;
        }, 1000);
    });
</script>
""".replace("__JSCALL__", js_call)

html_content_2 = html_content_2.replace("</body>", js_trigger + "\n</body>")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context(viewport={"width": 1200, "height": 800})
    page = context.new_page()
    page.set_content(html_content_1)
    time.sleep(1.5)
    img_bytes_1 = page.screenshot()
    page.set_content(html_content_2)
    time.sleep(2.0)
    img_bytes_2 = page.screenshot()
    browser.close()

img1 = Image.open(io.BytesIO(img_bytes_1))
img2 = Image.open(io.BytesIO(img_bytes_2))
img1.save("plot1.png")
img2.save("plot2.png")

distance = imagehash.phash(img1) - imagehash.phash(img2)
print("Saved plot1.png (Python-side mutation before render)")
print("Saved plot2.png (JS-side restyle/relayout after render)")
print("pHash distance:", distance)

assert distance >= 3, "Reproducer did NOT reproduce: images are similar."
print("Bug reproduced: the two renderings differ.")
'''


def write_reproducer(seed_script, seed_path, path, prop,
                     original_value, mutated_value, brt_dir) -> str:
    """Write a standalone Python script that reproduces the rendering bug.

    Returns the path to the written reproducer file.
    """
    fine_ts     = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    process_tag = mp.current_process().name.replace("-", "_")
    seed_stem   = os.path.splitext(os.path.basename(seed_path))[0]
    prop_tag    = re.sub(r"\W+", "_", prop)
    out_name    = f"{seed_stem}__{prop_tag}__{fine_ts}__{process_tag}.py"
    out_path    = os.path.join(brt_dir, out_name)

    header = (
        "# =============================================================================\n"
        "# Bug reproducer — auto-generated by Plotly Mutator\n"
        f"# Generated  : {datetime.now().isoformat(timespec='seconds')}\n"
        f"# Seed file  : {seed_path}\n"
        f"# Elem path  : {path}\n"
        f"# Property   : {prop}\n"
        f"# Original   : {original_value!r}\n"
        f"# Mutated    : {mutated_value!r}\n"
        "# =============================================================================\n"
    )

    # The seed already carries its own deterministic random/numpy seeding and
    # defines `fig` at module level — embed it verbatim.
    seed_block = (
        "# ── Original seed (deterministic) ────────────────────────────────────────────\n"
        f"{seed_script}\n"
        "# ── End of original seed ─────────────────────────────────────────────────────\n"
    )

    # Mutation context as valid Python expressions (special floats / numpy safe).
    params = (
        f"_PATH     = {path!r}\n"
        f"_PROP     = {prop!r}\n"
        f"_ORIGINAL = {safe_value_repr(original_value)}\n"
        f"_MUTATED  = {safe_value_repr(mutated_value)}\n"
    )

    reproducer = header + "\n" + seed_block + "\n" + params + _REPRODUCER_BODY

    with open(out_path, "w") as f:
        f.write(reproducer)

    print(f"[{mp.current_process().name}] Reproducer written -> {out_path}")
    return out_path


# ---------------------------------------------------------------------------
# Reproducer validation
# ---------------------------------------------------------------------------

def validate_reproducer(reproducer_path: str, timeout: int = 180) -> bool:
    """Run the reproducer in a subprocess; keep it only if it cleanly reproduces.

    A non-zero exit (e.g. the ``distance >= 3`` assertion failing, or an invalid
    mutation raising a ValueError on setattr) or a Python traceback marks the
    reproducer invalid: the file is deleted and ``False`` is returned.
    """
    process_name = mp.current_process().name
    try:
        result = subprocess.run(
            [sys.executable, reproducer_path],
            capture_output=True, text=True, timeout=timeout,
        )
        combined = result.stdout + result.stderr
        if result.returncode != 0 or "Traceback (most recent call last)" in combined:
            print(f"[{process_name}] Reproducer did not reproduce / errored "
                  f"— removing: {reproducer_path}")
            os.remove(reproducer_path)
            return False
    except subprocess.TimeoutExpired:
        print(f"[{process_name}] Reproducer timed out after {timeout}s "
              f"— removing: {reproducer_path}")
        os.remove(reproducer_path)
        return False
    except Exception as e:
        print(f"[{process_name}] Error validating {reproducer_path}: {e} — removing")
        os.remove(reproducer_path)
        return False

    print(f"[{process_name}] Reproducer validated OK -> {reproducer_path}")
    return True


# ---------------------------------------------------------------------------
# Per-test runner — called natively inside a completely fresh process
# ---------------------------------------------------------------------------

def run_test(seed_path, random_seed, dst_dir, brt_dir, threshold) -> None:
    """Execute one mutation test in a pristine (maxtasksperchild=1) process."""
    process_name = mp.current_process().name
    print("-" * 80)
    print(f"[{process_name}] {seed_path}")

    try:
        with open(seed_path) as f:
            raw = f.read()
        seed_script = prepare_seed(raw)

        # Single namespace so functions/comprehensions in the seed see globals.
        ns = {}
        exec(seed_script, ns)
        fig = ns.get("fig")
        if fig is None:
            print(f"[{process_name}] Seed did not define 'fig' — skipping")
            return

        # Seed exec pins random->42; reseed AFTER exec so sampling varies per
        # test while the figure itself stays deterministic (prototype order).
        random.seed(random_seed)

        mutate_fig(fig, threshold)

    except MutationRenderError as e:
        print(f"[{process_name}] Rendering difference detected: {e}")

        reproducer_path = write_reproducer(
            seed_script=seed_script,
            seed_path=seed_path,
            path=e.path,
            prop=e.prop,
            original_value=e.original_value,
            mutated_value=e.mutated_value,
            brt_dir=brt_dir,
        )
        if validate_reproducer(reproducer_path):
            # Persist the diverging screenshots as artefacts.
            try:
                if e.img1 is not None and e.img2 is not None:
                    tag = re.sub(r"\W+", "_", f"{e.path}.{e.prop}")
                    ts  = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
                    e.img1.save(os.path.join(dst_dir, f"{tag}__{ts}__plot1.png"))
                    e.img2.save(os.path.join(dst_dir, f"{tag}__{ts}__plot2.png"))
            except Exception as save_err:
                print(f"[{process_name}] Could not save artefact images: {save_err}")
            

    except Exception as e:
        print(f"[{process_name}] Error for seed {seed_path}: {e}")


def _task_wrapper(args):
    """Simple unpacking wrapper for imap_unordered."""
    try:
        run_test(*args)
    except Exception as e:
        print(f"[{mp.current_process().name}] Unhandled worker error: {e}")


def _generate_tasks(seed_paths, master_rng, dst_dir, brt_dir, threshold):
    """Infinite generator of tasks fed into the process pool."""
    while True:
        seed_path = master_rng.choice(seed_paths)
        seed_val  = master_rng.randint(0, 2**32 - 1)
        yield (seed_path, seed_val, dst_dir, brt_dir, threshold)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Plotly Mutator (Multi-processing)")
    parser.add_argument("--seed_dir", default="seeds/plotly",
                        help="Directory containing seed files")
    parser.add_argument("--seed", type=int, default=42,
                        help="Master seed for random mutations")
    parser.add_argument("--dst_dir", default="brt_workflow_plotly",
                        help="Directory to save artefacts from failed mutations")
    parser.add_argument("--max_workers", type=int, default=4,
                        help="Number of parallel worker processes")
    parser.add_argument("--threshold", type=int, default=3,
                        help="pHash distance below which images are 'similar'")
    args = parser.parse_args()

    seed_paths = list(get_seeds(args.seed_dir))
    if not seed_paths:
        print(f"No usable seed files found in {args.seed_dir}")
        return

    master_rng = random.Random(args.seed)

    time_str = get_time_str()
    dst_dir = f"{args.dst_dir}/{time_str}"
    brt_dir = f"./brt_workflow_plotly/{time_str}"
    os.makedirs(dst_dir, exist_ok=True)
    os.makedirs(brt_dir, exist_ok=True)

    print(f"Found {len(seed_paths)} seed files in {args.seed_dir}")
    print(f"Saving failed mutation artefacts to {dst_dir}")
    print(f"Saving bug reproducers           to {brt_dir}")
    print(f"Master seed: {args.seed}")
    print(f"Worker processes: {args.max_workers}")
    print(f"pHash threshold: {args.threshold}")

    # maxtasksperchild=1 tears down each worker after 1 task -> pristine state
    # (fresh Plotly UID counters, no leaked Playwright/browser handles).
    pool = mp.Pool(processes=args.max_workers, maxtasksperchild=1)
    tasks = _generate_tasks(seed_paths, master_rng, dst_dir, brt_dir, args.threshold)

    try:
        for _ in pool.imap_unordered(_task_wrapper, tasks):
            pass
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt received — signalling workers to stop…")
        pool.terminate()
        pool.join()


if __name__ == "__main__":
    # 'spawn' guarantees zero shared state inheritance and is required for
    # Playwright to launch cleanly inside each worker.
    mp.set_start_method("spawn", force=True)
    main()
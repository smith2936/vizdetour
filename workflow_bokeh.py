import argparse, math, os, random, json, imagehash, sys, subprocess
import multiprocessing as mp
from datetime import datetime
from bokeh.io.export import get_screenshot_as_png
from bokeh.models import CustomJS
from bokeh.events import DocumentReady
from bokeh.document import Document
from bokeh.core.property.primitive import Bool, Bytes, Complex, Float, Int, Null, String
from bokeh.core.property.bases import ParameterizedProperty
from bokeh.core.property.enum import Enum
from bokeh.core.property.nullable import Nullable
from utils_bokeh import (
    JS_ERROR_PRONE_FLOATS, JS_ERROR_PRONE_INTS,
    ERROR_PRONE_FLOAT_MULTIPLIERS, ERROR_PRONE_INT_MULTIPLIERS,
    JS_ERROR_PRONE_STRINGS,
)

# ---------------------------------------------------------------------------
# Patch curdoc() to be process-local BEFORE any seed file is ever exec'd.
#
# Since maxtasksperchild=1 ensures a fresh process per test, we can just use 
# a global variable to store the document for the current test run.
# ---------------------------------------------------------------------------
_process_doc = None


def _process_curdoc() -> Document:
    """Return the Document associated with the current process."""
    global _process_doc
    if _process_doc is None:
        _process_doc = Document()
    return _process_doc


import bokeh.io as _bokeh_io
_bokeh_io.curdoc = _process_curdoc


# ---------------------------------------------------------------------------
# Custom exception — carries mutation context so the catch-site can act on it
# ---------------------------------------------------------------------------

class MutationRenderError(AssertionError):
    """Raised when a no-op mutation produces a visible rendering difference."""

    def __init__(
        self,
        message: str,
        elem_id: str,
        prop: str,
        original_value,
        mutated_value,
    ) -> None:
        super().__init__(message)
        self.elem_id = elem_id
        self.prop = prop
        self.original_value = original_value
        self.mutated_value = mutated_value


# ---------------------------------------------------------------------------
# Core helpers
# ---------------------------------------------------------------------------

def safe_value_repr(value) -> str:
    """Return a string that is a valid Python *expression* for *value*.

    ``repr(float('inf'))`` yields ``'inf'``, which is not a valid Python
    literal.  This helper emits ``float('inf')`` instead.
    """
    if isinstance(value, float):
        if math.isnan(value):
            return "float('nan')"
        if math.isinf(value):
            return "float('inf')" if value > 0 else "float('-inf')"
    return repr(value)


def is_primitive(value) -> bool:
    """Return True if *value* is a primitive / immutable type."""
    return value is None or isinstance(
        value, (bool, int, float, str, bytes, tuple, frozenset)
    )


def mutate_doc(doc: Document, rng: random.Random) -> None:
    """Mutate one randomly chosen primitive property of a random model in *doc*."""
    process_name = mp.current_process().name

    ids = list(doc.models._models)
    elem = doc.models._models[rng.choice(ids)]
    props = list(elem.properties())

    # Try up to 5 times to land on a property whose current value is primitive.
    for _ in range(5):
        prop = rng.choice(props)
        if is_primitive(getattr(elem, prop)):
            break

    original_value = getattr(elem, prop)
    print(f"[{process_name}] Selected element: {elem}, Property: {prop}")

    prop_type = elem.properties(_with_props=True)[prop]
    print(f"[{process_name}] Property type: {prop_type}")

    def get_mutation_values(pt):
        mutation_values = []
        if isinstance(pt, ParameterizedProperty):
            for tp in pt._type_params:
                mutation_values.extend(get_mutation_values(tp))
        if isinstance(pt, Nullable):
            mutation_values.append(None)
            pt = pt._type_params[0]
        if isinstance(pt, Enum):
            mutation_values.extend(pt.allowed_values)
        elif isinstance(pt, Bool):
            mutation_values += (
                [not original_value] if isinstance(original_value, bool) else [True, False]
            )
        elif isinstance(pt, Int):
            mutation_values.append(
                rng.choice(JS_ERROR_PRONE_INTS)
                + rng.choice(ERROR_PRONE_INT_MULTIPLIERS) * original_value
                if isinstance(original_value, int)
                else rng.choice(JS_ERROR_PRONE_INTS)
            )
        elif isinstance(pt, Float):
            mutation_values.append(
                rng.choice(JS_ERROR_PRONE_FLOATS)
                + rng.choice(ERROR_PRONE_FLOAT_MULTIPLIERS) * original_value
                if isinstance(original_value, float)
                else rng.choice(JS_ERROR_PRONE_FLOATS)
            )
        elif isinstance(pt, String):
            mutation_values.append(rng.choice(JS_ERROR_PRONE_STRINGS))
        elif isinstance(pt, Bytes):
            mutation_values += (
                [original_value + b"_mutated"]
                if isinstance(original_value, bytes)
                else [b"mutated"]
            )
        elif isinstance(pt, Complex):
            mutation_values += (
                [complex(original_value.real + 1, original_value.imag + 1)]
                if isinstance(original_value, complex)
                else [complex(1, 1)]
            )
        elif isinstance(pt, Null):
            mutation_values += [None]
        return mutation_values

    mutation_values = list(set(get_mutation_values(prop_type) + [original_value]))
    print(f"[{process_name}] Mutation candidates for {prop}: {mutation_values}")

    mutated_value = rng.choice(mutation_values)
    print(f"[{process_name}] Original: {original_value!r}, Mutated: {mutated_value!r}")

    # --- screenshot before render ---
    setattr(elem, prop, mutated_value)
    img1 = get_screenshot_as_png(doc)
    setattr(elem, prop, original_value)

    # --- screenshot after render ---
    doc.js_on_event(
        DocumentReady,
        CustomJS(
            args=dict(elem=elem),
            code=f"elem.{prop} = {json.dumps(mutated_value)};",
        ),
    )
    img2 = get_screenshot_as_png(doc)

    # Raise a structured exception instead of a bare assert so callers can
    # inspect elem_id / prop / values without re-running the test.
    if not images_similar(img1, img2, threshold=3):
        raise MutationRenderError(
            f"No-op mutation changed image via resetting {prop} of {elem} "
            f"to {mutated_value!r} before and after render",
            elem_id=elem.id,
            prop=prop,
            original_value=original_value,
            mutated_value=mutated_value,
        )


def images_similar(img1, img2, threshold: int = 3) -> bool:
    return imagehash.phash(img1) - imagehash.phash(img2) < threshold


def get_time_str() -> str:
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def get_seeds(seed_dir: str):
    for file in os.listdir(seed_dir):
        if not file.endswith(".py"):
            continue
        path = os.path.join(seed_dir, file)
        with open(path) as f:
            code = f.read()
        if ".add_root(" in code:
            yield path
        else:
            print(f"Skipping {path}: no Bokeh document root found")


# ---------------------------------------------------------------------------
# Bug-reproducer writer
# ---------------------------------------------------------------------------

def write_reproducer(
    seed_path: str,
    elem_id: str,
    prop: str,
    original_value,
    mutated_value,
    brt_bokeh_dir: str,
) -> str:
    """Write a standalone Python script that reproduces the rendering bug.

    Returns the path to the written reproducer file.
    """
    with open(seed_path) as f:
        seed_code = f.read()

    # Escape braces so the seed code survives being embedded inside an f-string.
    safe_seed = seed_code.replace("{", "{{").replace("}", "}}")

    # Use microsecond precision + process name to avoid filename collisions
    fine_ts = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    process_tag = mp.current_process().name.replace("-", "_")
    seed_stem = os.path.splitext(os.path.basename(seed_path))[0]
    out_name = f"{seed_stem}__{prop}__{fine_ts}__{process_tag}.py"
    out_path = os.path.join(brt_bokeh_dir, out_name)

    # Build the CustomJS code line; fall back to a comment if the value cannot
    # be round-tripped through JSON (e.g. bytes, complex).
    try:
        json_mutated = json.dumps(mutated_value)
        js_code_line = f'        code="""elem.{prop} = {json_mutated};""",'
    except (TypeError, ValueError):
        js_code_line = (
            f"        # NOTE: mutated_value {mutated_value!r} is not "
            "JSON-serialisable — JS-side mutation is omitted."
        )

    # Use safe_value_repr so special floats (inf, nan) become valid expressions.
    orig_expr = safe_value_repr(original_value)
    mut_expr  = safe_value_repr(mutated_value)

    reproducer = f"""\
# =============================================================================
# Bug reproducer — auto-generated by Bokeh Mutator
# Generated  : {datetime.now().isoformat(timespec='seconds')}
# Seed file  : {seed_path}
# Element ID : {elem_id}
# Property   : {prop}
# Original   : {original_value!r}
# Mutated    : {mutated_value!r}
# =============================================================================
import json
import bokeh.io as _bokeh_io
from bokeh.document import Document
from bokeh.io.export import get_screenshot_as_png
from bokeh.models import CustomJS
from bokeh.events import DocumentReady

# Patch curdoc() so the seed code runs without a live Bokeh server.
_doc = Document()
_bokeh_io.curdoc = lambda: _doc

# ── Original seed ─────────────────────────────────────────────────────────────
{safe_seed}
# ── End of original seed ──────────────────────────────────────────────────────

doc = _doc

# Locate the specific model that triggered the bug using its stable ID.
_elem_id = {elem_id!r}
elem = next(m for m in doc.models if m.id == _elem_id)

original_value = {orig_expr}
mutated_value  = {mut_expr}

# ── Screenshot 1 : Python-side mutation applied before rendering ──────────────
elem.{prop} = mutated_value
img1 = get_screenshot_as_png(doc)
img1.save("plot1.png")

# Restore the original value so the document is in a clean state.
elem.{prop} = original_value

# ── Screenshot 2 : JS callback applies the same mutation after DocumentReady ──
doc.js_on_event(
    DocumentReady,
    CustomJS(
        args=dict(elem=elem),
{js_code_line}
    ),
)
img2 = get_screenshot_as_png(doc)
img2.save("plot2.png")

print("Saved plot1.png  (Python-side mutation before render)")
print("Saved plot2.png      (JS-side mutation via DocumentReady)")
print("The two images differ — that is the bug.")
"""

    with open(out_path, "w") as f:
        f.write(reproducer)

    print(f"[{mp.current_process().name}] Reproducer written → {out_path}")
    return out_path


# ---------------------------------------------------------------------------
# Reproducer validation
# ---------------------------------------------------------------------------

def validate_reproducer(reproducer_path: str, timeout: int = 120) -> bool:
    """Run the reproducer script in a subprocess and check for Bokeh
    validation errors.

    If ``ERROR:bokeh.core.validation.check`` appears in stdout or stderr the
    reproducer is considered invalid: the file is deleted and the function
    returns ``False``.  Otherwise it returns ``True``.
    """
    process_name = mp.current_process().name
    try:
        result = subprocess.run(
            [sys.executable, reproducer_path],
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        combined_output = result.stdout + result.stderr
        if "ERROR:bokeh.core.validation.check" in combined_output:
            print(
                f"[{process_name}] Reproducer has Bokeh validation errors "
                f"— removing: {reproducer_path}"
            )
            os.remove(reproducer_path)
            return False
    except subprocess.TimeoutExpired:
        print(
            f"[{process_name}] Reproducer timed out after {timeout}s "
            f"— removing: {reproducer_path}"
        )
        os.remove(reproducer_path)
        return False
    except Exception as e:
        print(
            f"[{process_name}] Error validating reproducer "
            f"{reproducer_path}: {e} — removing"
        )
        os.remove(reproducer_path)
        return False

    print(f"[{process_name}] Reproducer validated OK → {reproducer_path}")
    return True


# ---------------------------------------------------------------------------
# Per-test runner — called natively inside a completely fresh process
# ---------------------------------------------------------------------------

def run_test(
    seed_path: str,
    random_seed: int,
    dst_dir: str,
    brt_bokeh_dir: str,
) -> None:
    """
    Execute one mutation test. Because maxtasksperchild=1, this function 
    always runs in a pristine Python environment.
    """
    process_name = mp.current_process().name
    print("-" * 80)
    print(f"[{process_name}] {seed_path}")

    # Set the global process doc to guarantee curdoc() functions.
    global _process_doc
    _process_doc = Document()
    
    # Reinitialize the random generator with the seed passed down from main loop
    rng = random.Random(random_seed)

    with open(seed_path) as f:
        code = f.read()

    try:
        ns = {"__builtins__": __builtins__}
        exec(code, ns)
        mutate_doc(_process_doc, rng)
    except MutationRenderError as e:
        print(f"[{process_name}] Rendering difference detected: {e}")
        reproducer_path = write_reproducer(
            seed_path=seed_path,
            elem_id=e.elem_id,
            prop=e.prop,
            original_value=e.original_value,
            mutated_value=e.mutated_value,
            brt_bokeh_dir=brt_bokeh_dir,
        )
        validate_reproducer(reproducer_path)
    except Exception as e:
        print(f"[{process_name}] Error for seed {seed_path}: {e}")


def _task_wrapper(args):
    """Simple unpacking wrapper for imap_unordered."""
    try:
        run_test(*args)
    except Exception as e:
        print(f"[{mp.current_process().name}] Unhandled worker error: {e}")


def _generate_tasks(seed_paths, master_rng, dst_dir, brt_bokeh_dir):
    """Infinite generator of tasks fed into the process pool."""
    while True:
        seed_path = master_rng.choice(seed_paths)
        seed_val = master_rng.randint(0, 2**32 - 1)
        yield (seed_path, seed_val, dst_dir, brt_bokeh_dir)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Bokeh Mutator (Multi-processing)")
    parser.add_argument("--seed_dir", default="seeds/bokeh",
                        help="Directory containing seed files")
    parser.add_argument("--seed", type=int, default=42,
                        help="Master seed for random mutations")
    parser.add_argument("--dst_dir", default="brt_workflow_bokeh",
                        help="Directory to save artefacts from failed mutations")
    parser.add_argument("--max_workers", type=int, default=4,
                        help="Number of parallel worker processes")
    args = parser.parse_args()

    seed_paths = list(get_seeds(args.seed_dir))
    master_rng = random.Random(args.seed)

    time_str = get_time_str()
    dst_dir       = f"{args.dst_dir}/{time_str}"
    brt_bokeh_dir = f"./brt_workflow_bokeh/{time_str}"

    os.makedirs(dst_dir, exist_ok=True)
    os.makedirs(brt_bokeh_dir, exist_ok=True)

    print(f"Found {len(seed_paths)} seed files in {args.seed_dir}")
    print(f"Saving failed mutated files to {dst_dir}")
    print(f"Saving bug reproducers    to {brt_bokeh_dir}")
    print(f"Master seed: {args.seed}")
    print(f"Worker processes: {args.max_workers}")

    # Set up process pool. maxtasksperchild=1 tears down the Python process 
    # completely after 1 task, guaranteeing a completely reset Bokeh ID generator.
    pool = mp.Pool(processes=args.max_workers, maxtasksperchild=1)
    tasks = _generate_tasks(seed_paths, master_rng, dst_dir, brt_bokeh_dir)

    try:
        # imap_unordered pulls tasks lazily, so our infinite generator is safe here.
        for _ in pool.imap_unordered(_task_wrapper, tasks):
            pass
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt received — signalling workers to stop…")
        pool.terminate()
        pool.join()


if __name__ == "__main__":
    # Force 'spawn' to ensure cross-platform consistency and zero shared state
    # inheritance from the main process.
    mp.set_start_method("spawn", force=True)
    main()
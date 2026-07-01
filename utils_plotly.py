# Reference: _plotly_utils/basevalidators.py
import itertools
import re
import sys
from typing import List
import random


def _regex_examples(pattern: str) -> List:
    """Generate example strings for common plotly regex patterns."""
    # Subplot anchor patterns: ^x([2-9]|[1-9][0-9]+)?( domain)?$
    m = re.match(r"^\^(\w+)\(", pattern)
    if m:
        base = m.group(1)
        examples = [base, base + "2", base + "3"]
        if "domain" in pattern:
            examples.append(base + " domain")
        return examples
    # Dash length list: ^\d+(\.\d+)?(px|%)?((,|\s)\s*\d+...)*$
    if r"\d+" in pattern and ("px" in pattern or "%" in pattern):
        return ["5px,10px,2px,2px", "5 10 2 2", "2,4,6"]
    return []


def _number_candidates(
    min_val, max_val, has_min_max: bool, integer: bool = False
) -> List:
    """Generate interesting numeric candidates given optional min/max bounds."""
    _NEG_INF = float("-inf")
    _POS_INF = float("inf")
    _INT_MIN = -sys.maxsize - 1
    _INT_MAX = sys.maxsize

    if not has_min_max:
        return [0, 1, 2, -1, 10] if integer else [0, 0.5, 1.0, -1.0, 10.0]

    lo = None if min_val in (None, _NEG_INF, _INT_MIN) else min_val
    hi = None if max_val in (None, _POS_INF, _INT_MAX) else max_val

    def cast(v):
        return int(v) if integer else float(v)

    seen = set()
    candidates = []

    def add(v):
        key = round(v, 10)
        if key not in seen:
            seen.add(key)
            candidates.append(cast(v))

    if lo is not None:
        add(lo)
    if hi is not None:
        add(hi)
    if lo is not None and hi is not None:
        add((lo + hi) / 2)

    # Add canonical values that fall within the range
    probe = [0, 1] if integer else [0.0, 0.25, 0.5, 0.75, 1.0]
    eff_lo = lo if lo is not None else _NEG_INF
    eff_hi = hi if hi is not None else _POS_INF
    for v in probe:
        if eff_lo <= v <= eff_hi:
            add(v)

    return candidates


def extractCandidates(validator) -> List:
    """
    Return a list of candidate values for the given BaseValidator instance.

    For validators with enumerable valid values (EnumeratedValidator,
    BooleanValidator, FlaglistValidator, etc.) all valid values are returned.
    For open-ended validators (NumberValidator, ColorValidator, etc.) a
    selection of interesting representative values is returned.
    """
    cls = type(validator).__name__

    # --- Enumerated (includes DashValidator which extends it) ---
    if cls in ("EnumeratedValidator", "DashValidator"):
        candidates = []
        for v, regex in zip(validator.values, validator.val_regexs):
            if regex is None:
                candidates.append(v)
            else:
                candidates.extend(_regex_examples(regex.pattern))
        return candidates

    # --- Boolean ---
    if cls == "BooleanValidator":
        return [True, False]

    # --- Number (float) ---
    if cls == "NumberValidator":
        return _number_candidates(
            validator.min_val, validator.max_val, validator.has_min_max, integer=False
        )

    # --- Integer ---
    if cls == "IntegerValidator":
        base = _number_candidates(
            validator.min_val, validator.max_val, validator.has_min_max, integer=True
        )
        extras = list(validator.extras)
        return extras + [v for v in base if v not in extras]

    # --- String ---
    if cls == "StringValidator":
        candidates = ["Courier New", "Times New Roman", "Arial", "Courier New, monospace", "Comic Sans MS", "serif", "sans-serif", "cursive", "fantasy", "monospace"]
        if validator.values:
            return candidates + list(validator.values)
        if validator.no_blank:
            return candidates + ["text", "label", "title"]
        return candidates + ["", "text", "label", "42"]

    # --- Color ---
    if cls == "ColorValidator":
        candidates = [
            "red", "blue", "green", "black", "white",
            "#ff0000", "#00ff00", "#0000ff",
            "rgb(255,0,0)", "rgba(0,128,0,0.5)",
            "hsl(240,100%,50%)",
        ]
        if validator.numbers_allowed():
            candidates.extend([0, 0.5, 1.0])
        return candidates

    # --- Colorlist ---
    if cls == "ColorlistValidator":
        return [
            ["red", "blue", "green"],
            ["#ff0000", "#00ff00", "#0000ff"],
        ]

    # --- Colorscale ---
    if cls == "ColorscaleValidator":
        candidates = list(validator.named_colorscales)
        candidates = random.sample(candidates, min(len(candidates), 5))  # limit to 5 named scales
        candidates_r = [candidate + "_r" for candidate in candidates] # appending '_r' to a named colorscale reverses it
        return [
            "Viridis", "Plasma", "Blues", "Reds", "RdBu", "Jet", "Hot",
            [[0, "blue"], [0.5, "white"], [1.0, "red"]],
            ["blue", "white", "red"],
            *candidates,
            *candidates_r,
        ]

    # --- Angle: valid range is (-180, 180], values outside are wrapped ---
    if cls == "AngleValidator":
        return [-180, -90, -45, 0, 45, 90, 135, 180]

    # --- Subplot ID ---
    if cls == "SubplotidValidator":
        base = validator.base
        return [base, base + "2", base + "3"]

    # --- Flaglist ---
    if cls == "FlaglistValidator":
        flags = list(validator.flags)
        extras = list(validator.extras)
        candidates = list(extras)
        candidates.extend(flags)
        for a, b in itertools.combinations(flags, 2):
            candidates.append(a + "+" + b)
        if 2 < len(flags) <= 8:
            candidates.append("+".join(flags))
        return candidates

    # --- Any ---
    if cls == "AnyValidator":
        if validator.values:
            return list(validator.values)
        return [None, True, False, 0, 1.0, "text", [], {}]

    # --- InfoArray: recurse into item validators to build example arrays ---
    if cls == "InfoArrayValidator":
        item_candidates = [extractCandidates(iv) for iv in validator.item_validators]
        if not all(item_candidates):
            return [[]]
        example_1d = [cands[0] for cands in item_candidates]
        if validator.dimensions == 1:
            return [example_1d]
        elif validator.dimensions == 2:
            return [[example_1d]]
        else:  # "1-2": accept both 1D and 2D
            return [example_1d, [example_1d]]

    # --- Literal: only the fixed value is valid ---
    if cls == "LiteralValidator":
        return [validator.val]

    # --- Image URI ---
    if cls == "ImageUriValidator":
        return [
            "https://example.com/image.png",
            # 1×1 transparent PNG encoded as data URI
            "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJ"
            "AAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg==",
        ]

    # --- DataArray ---
    if cls == "DataArrayValidator":
        return [
            [1, 2, 3],
            [0.0, 0.5, 1.0],
            ["a", "b", "c"],
        ]

    # --- Source (chart studio column reference) ---
    if cls == "SrcValidator":
        return ["source_id"]

    # --- Compound objects: pass an empty dict; the validator fills in defaults ---
    if cls in ("CompoundValidator", "TitleValidator"):
        return [{}]

    # --- Compound arrays ---
    if cls == "CompoundArrayValidator":
        return [[]]

    # --- Trace data ---
    if cls == "BaseDataValidator":
        return [[]]

    # --- Template ---
    if cls == "BaseTemplateValidator":
        return [{}]

    # Fallback for unknown subclasses
    return []

import random

def _is_element(obj):
    return hasattr(obj, "_valid_props")

class ElementTree:
    class Node:
        __slots__ = ("obj", "path", "children")
        def __init__(self, obj, path):
            self.obj = obj
            self.path = path
            self.children = []

    # Property names to NOT descend into. 'template' is the big offender:
    # it carries default styling for every trace type and dominates sampling.
    DEFAULT_SKIP = frozenset({"template"})

    def __init__(self, fig, include_empty=True, skip_props=None):
        self.include_empty = include_empty
        self.skip = self.DEFAULT_SKIP if skip_props is None else frozenset(skip_props)

        self.root = self.Node(fig, "fig")
        for i, trace in enumerate(fig.data):
            if _is_element(trace):
                self.root.children.append(self._build(trace, f"fig.data[{i}]"))
        if _is_element(fig.layout):
            self.root.children.append(self._build(fig.layout, "fig.layout"))

        self.nodes = []
        self._flatten(self.root)

        # Only nodes that ARE elements (have _valid_props) are valid mutation targets.
        # This drops the root `fig` (no _valid_props) automatically.
        self.elem_nodes   = [n for n in self.nodes if _is_element(n.obj)]
        self._weights = [max(len(self._scalar_props(n.obj)), 1) for n in self.elem_nodes]
        self.data_nodes   = [n for n in self.elem_nodes if n.path.startswith("fig.data[")]
        self.layout_nodes = [n for n in self.elem_nodes if n.path.startswith("fig.layout")]

    def _has_data(self, obj):
        try:
            return bool(obj._props)
        except Exception:
            return True

    def _keep(self, child):
        return self.include_empty or self._has_data(child)

    def _build(self, obj, path):
        node = self.Node(obj, path)
        for prop in sorted(obj._valid_props):
            if prop in self.skip:                 # <-- prune template (and any user skips)
                continue
            try:
                val = getattr(obj, prop)
            except Exception:
                continue
            if val is None:
                continue
            if _is_element(val):
                if self._keep(val):
                    node.children.append(self._build(val, f"{path}.{prop}"))
            elif isinstance(val, (list, tuple)):
                for i, item in enumerate(val):
                    if _is_element(item) and self._keep(item):
                        node.children.append(self._build(item, f"{path}.{prop}[{i}]"))
        return node

    def _flatten(self, node):
        self.nodes.append(node)
        for c in node.children:
            self._flatten(c)

    def __len__(self):
        return len(self.nodes)

    def _scalar_props(self, obj):
        """Mutatable scalar props = valid props that aren't elements/element-lists and aren't skipped."""
        out = []
        for prop in obj._valid_props:
            if prop in self.skip:
                continue
            try:
                val = getattr(obj, prop)
            except Exception:
                continue
            if _is_element(val):
                continue
            if isinstance(val, (list, tuple)) and any(_is_element(v) for v in val):
                continue
            out.append(prop)
        return out

    def sample(self, rng=random):
        node = rng.choices(self.elem_nodes, weights=self._weights, k=1)[0]
        return node.obj, node.path

    def sample_stratified(self, rng=random):
        # 50% data, 50% layout
        if not self.data_nodes or not self.layout_nodes:
            return self.sample(rng)
        if rng.random() < 0.5:
            node = rng.choice(self.data_nodes)
        else:
            node = rng.choice(self.layout_nodes)
        return node.obj, node.path

    def print_tree(self, node=None, depth=0):
        node = node or self.root
        print("  " * depth + node.path)
        for c in node.children:
            self.print_tree(c, depth + 1)
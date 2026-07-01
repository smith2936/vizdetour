
JS_ERROR_PRONE_STRINGS = [
    # Prototype pollution
    "__proto__", "constructor", "prototype",
    "__defineGetter__", "__defineSetter__",
    "hasOwnProperty", "toString", "valueOf",

    # Type coercion / JSON edge cases
    "null", "undefined", "NaN", "Infinity", "-Infinity",
    "true", "false", "[]", "{}", "[object Object]",

    # Numeric string coercion
    "0", "1", "-1", ".1", "-0", "0.0",
    "1e308", "-1e308", "0x10", "0b1010",

    # Whitespace / blank-ish strings
    "", " ", "\t", "\n", "\r", "\r\n",

    # Unicode edge cases
    "\u0000",       # null byte
    "\uFEFF",       # BOM / zero-width no-break space
    "\u202e",       # right-to-left override
    "\u200b",       # zero-width space
    "\u200d",       # zero-width joiner
    "\uffff",       # non-character
    "\ud800",       # lone high surrogate (invalid UTF-16)
    "💀" * 50,      # multi-byte emoji stress

    # XSS / HTML injection
    "<script>alert(1)</script>",
    "<img src=x onerror=alert(1)>",
    "&#x3C;script&#x3E;",

    # Template / format string injection
    "${7*7}",       # JS template literal
    "{{7*7}}",      # common template engine (Jinja2, Handlebars)
    "<%= 7*7 %>",   # ERB / EJS
    "%s%s%s%n",     # C-style format string

    # SQL injection fragments
    "' OR '1'='1", "'; DROP TABLE users;--",

    # Path traversal
    "../../../etc/passwd",
    "..\\..\\..\\windows\\system32",

    # URL/protocol injection
    "javascript:void(0)",
    "data:text/html,<script>alert(1)</script>",

    # ReDoS-prone input
    "a" * 100 + "!",

    # Long strings
    "mut" * 10,
    "a" * 1000,
]
JS_ERROR_PRONE_FLOATS = [
    # IEEE 754 special values
    float("inf"),
    float("-inf"),
    float("nan"),

    # Signed zero
    0.0,
    -0.0,

    # Float precision edge cases
    0.1 + 0.2,              # 0.30000000000000004
    1.0 / 3.0,
    2.0 ** 53,              # Number.MAX_SAFE_INTEGER + 1
    2.0 ** 53 + 1,
    -(2.0 ** 53),
    -(2.0 ** 53) - 1,

    # JS Number boundaries
    1.7976931348623157e+308,     # Number.MAX_VALUE
    -1.7976931348623157e+308,
    5e-324,                      # Number.MIN_VALUE
    2.2250738585072014e-308,     # denormalized boundary

    # Overflow / underflow
    1.7976931348623157e+308 * 2, # → Infinity
    5e-324 / 2,                  # → 0.0

    # Near-zero
    1e-300,
    -1e-300,

    # Common values
    1.0, -1.0, 0.5, -0.5,

    # ULP boundary around 1
    1.0000000000000002,          # smallest float > 1.0
    1.0000000000000001,          # collapses to 1.0 in JS
    100000000000000016.0,        # representation drift at scale
]
ERROR_PRONE_FLOAT_MULTIPLIERS = [
    0.0,                    # annihilation → always 0
    -0.0,                   # signed zero annihilation → -0
    1.0,                    # identity — baseline sanity check
    -1.0,                   # negation
    1.0000000000000002,     # 1 ULP above 1 — off-by-epsilon scale
    0.9999999999999998,     # 1 ULP below 1 — off-by-epsilon scale
    1.1,                    # slight scale up — accumulates rounding drift
    0.9,                    # slight scale down — accumulates rounding drift
    2.0,                    # doubling — may overflow near MAX_VALUE
    0.5,                    # halving — may underflow near MIN_VALUE
    2.0 ** 53,              # pushes value past integer precision boundary
    float("inf"),           # → Infinity, or NaN if original_value is 0
    float("nan"),           # → NaN regardless of original
    1e-300,                 # near-zero scale — pushes toward denormal/underflow
    -1e-300,                # near-zero negative scale
]
JS_ERROR_PRONE_INTS = [
    # Zero and near-zero
    0, 1, -1, 2, -2,

    # 32-bit signed int boundaries (ALL JS bitwise operators truncate to int32)
    2**31 - 1,       # INT32_MAX = 2147483647
    2**31,           # INT32_MAX + 1 — wraps to INT32_MIN in bitwise context
    -(2**31),        # INT32_MIN = -2147483648
    -(2**31) - 1,    # INT32_MIN - 1

    # 32-bit unsigned boundary (>>> zero-fill right shift converts to uint32)
    2**32 - 1,       # UINT32_MAX = 4294967295 — also what (-1 >>> 0) yields in JS
    2**32,           # UINT32_MAX + 1

    # Array length boundary (max JS array length is 2^32 - 1 elements)
    2**32 - 2,       # largest valid array index

    # JS float64 integer precision boundary
    2**53 - 1,       # Number.MAX_SAFE_INTEGER
    2**53,           # MAX_SAFE_INTEGER + 1 — indistinguishable from MAX_SAFE_INTEGER in JS
    2**53 + 1,       # collapses to MAX_SAFE_INTEGER in JS
    -(2**53 - 1),    # Number.MIN_SAFE_INTEGER
    -(2**53),
    -(2**53) - 1,    # collapses to MIN_SAFE_INTEGER in JS

    # Typed array overflow boundaries
    127, 128,        # Int8Array: 128 wraps to -128
    -128, -129,      # Int8Array: -129 wraps to 127
    255, 256,        # Uint8Array: 256 wraps to 0
    32767, 32768,    # Int16Array: 32768 wraps to -32768
    -32768, -32769,  # Int16Array: -32769 wraps to 32767
    65535, 65536,    # Uint16Array: 65536 wraps to 0

    # Powers of 2 — common bitmask and left-shift targets
    # notably: 1 << 31 becomes -2147483648 (INT32_MIN) in JS
    *[2**i for i in range(2, 31)],   # 4, 8, ..., 2^30
]
ERROR_PRONE_INT_MULTIPLIERS = [
    0,        # annihilation → always 0
    1,        # identity
    -1,       # negation
    2,        # doubling — overflows int32 for values near INT32_MAX
    -2,       # negative doubling
    2**31,    # pushes any non-zero value past MAX_SAFE_INTEGER
    2**53,    # guaranteed JS float64 precision loss
]

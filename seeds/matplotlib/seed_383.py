import warnings
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import LineCollection

def colored_line_between_pts(x, y, c, ax, **lc_kwargs):
    if "array" in lc_kwargs:
        warnings.warn(
            'The provided "array" keyword argument will be overridden',
            UserWarning,
            stacklevel=2,
        )

    if len(c) != len(x) - 1:
        warnings.warn(
            "The c argument should have a length one less than the length of x and y. "
            "If it has the same length, use the colored_line function instead.",
            UserWarning,
            stacklevel=2,
        )

    points = np.array([x, y]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    lc = LineCollection(segments, **lc_kwargs)

    lc.set_array(c)

    return ax.add_collection(lc)


x = np.linspace(0, 3 * np.pi, 500)
y = np.sin(x)
dydx = np.cos(0.5 * (x[:-1] + x[1:]))

fig2, ax2 = plt.subplots()
line = colored_line_between_pts(x, y, dydx, ax2, linewidth=2, cmap="viridis")
fig2.colorbar(line, ax=ax2, label="dy/dx")

ax2.set_xlim(x.min(), x.max())
ax2.set_ylim(-1.1, 1.1)
ax2.set_title("Color between points")

plt.show()
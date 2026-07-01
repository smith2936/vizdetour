import warnings
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import LineCollection

def colored_line(x, y, c, ax=None, **lc_kwargs):
    if "array" in lc_kwargs:
        warnings.warn(
            'The provided "array" keyword argument will be overridden',
            UserWarning,
            stacklevel=2,
        )

    xy = np.stack((x, y), axis=-1)
    xy_mid = np.concatenate(  # fixed typo: concat -> concatenate
        (xy[0, :][None, :], (xy[:-1, :] + xy[1:, :]) / 2, xy[-1, :][None, :]), axis=0
    )
    segments = np.stack((xy_mid[:-1, :], xy, xy_mid[1:, :]), axis=-2)

    lc_kwargs["array"] = c
    lc = LineCollection(segments, **lc_kwargs)

    ax = ax or plt.gca()
    ax.add_collection(lc)

    return lc


t = np.linspace(-7.4, -0.5, 200)
x = 0.9 * np.sin(t)
y = 0.9 * np.cos(1.6 * t)
color = np.linspace(0, 2, t.size)

fig1, ax1 = plt.subplots()
lines = colored_line(x, y, color, ax1, linewidth=10, cmap="plasma")
fig1.colorbar(lines)

ax1.set_title("Color at each point")

plt.show()
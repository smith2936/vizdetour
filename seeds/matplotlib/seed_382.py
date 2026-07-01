import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import LineCollection

def colored_line(x, y, c, ax=None, **lc_kwargs):
    import warnings
    if "array" in lc_kwargs:
        warnings.warn(
            'The provided "array" keyword argument will be overridden',
            UserWarning,
            stacklevel=2,
        )

    xy = np.stack((x, y), axis=-1)
    xy_mid = np.concatenate(
        (xy[0, :][None, :], (xy[:-1, :] + xy[1:, :]) / 2, xy[-1, :][None, :]), axis=0
    )
    segments = np.stack((xy_mid[:-1, :], xy, xy_mid[1:, :]), axis=-2)

    lc_kwargs["array"] = c
    lc = LineCollection(segments, **lc_kwargs)

    ax = ax or plt.gca()
    ax.add_collection(lc)

    return lc


x = [0, 1, 2, 3, 4]
y = [0, 1, 2, 1, 1]
c = [1, 2, 3, 4, 5]
fig, ax = plt.subplots()
ax.scatter(x, y, c=c, cmap='rainbow')
colored_line(x, y, c=c, ax=ax, cmap='rainbow')

plt.show()
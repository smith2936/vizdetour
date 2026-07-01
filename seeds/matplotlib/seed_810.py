import matplotlib.pyplot as plt
import numpy as np
from matplotlib import patheffects

arr = np.arange(25).reshape((5, 5))

fig, ax2 = plt.subplots(figsize=(2.5, 3))
ax2.imshow(arr)
cntr = ax2.contour(arr, colors="k")

cntr.set(path_effects=[patheffects.withStroke(linewidth=3, foreground="w")])

clbls = ax2.clabel(cntr, fmt="%2.0f", use_clabeltext=True)
plt.setp(clbls, path_effects=[
    patheffects.withStroke(linewidth=3, foreground="w")])

plt.show()
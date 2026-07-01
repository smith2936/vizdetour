import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches
import matplotlib.path as path

np.random.seed(19680801)  

data = np.random.randn(1000)
n, bins = np.histogram(data, 50)

left = bins[:-1]
right = bins[1:]
bottom = np.zeros(len(left))
top = bottom + n

XY = np.array([[left, left, right, right], [bottom, top, top, bottom]]).T

barpath = path.Path.make_compound_path_from_polys(XY)

patch = patches.PathPatch(barpath)
patch.sticky_edges.y[:] = [0]

fig, ax = plt.subplots()
ax.add_patch(patch)
ax.autoscale_view()
plt.show()
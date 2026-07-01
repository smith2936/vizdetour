import matplotlib.pyplot as plt
import numpy as np
from matplotlib import collections, transforms

nverts = 50
npts = 100

r = np.arange(nverts)
theta = np.linspace(0, 2*np.pi, nverts)
xx = r * np.sin(theta)
yy = r * np.cos(theta)
spiral = np.column_stack([xx, yy])

rs = np.random.RandomState(19680801)
xyo = rs.randn(npts, 2)
colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

fig, ax1 = plt.subplots()
col = collections.LineCollection(
    [spiral], offsets=xyo, offset_transform=ax1.transData, color=colors)
trans = fig.dpi_scale_trans + transforms.Affine2D().scale(1.0/72.0)
col.set_transform(trans)
ax1.add_collection(col)
ax1.set_title('LineCollection using offsets')

plt.show()
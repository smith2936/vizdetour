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

fig, ax3 = plt.subplots()
col = collections.RegularPolyCollection(
    7, sizes=np.abs(xx) * 10.0, offsets=xyo, offset_transform=ax3.transData,
    color=colors)
trans = transforms.Affine2D().scale(fig.dpi / 72.0)
col.set_transform(trans)
ax3.add_collection(col)
ax3.set_title('RegularPolyCollection using offsets')

plt.show()
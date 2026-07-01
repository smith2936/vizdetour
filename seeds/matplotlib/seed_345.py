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

fig, ax2 = plt.subplots()
col = collections.PolyCollection(
    [spiral], offsets=xyo, offset_transform=ax2.transData, color=colors)
trans = transforms.Affine2D().scale(fig.dpi/72.0)
col.set_transform(trans)
ax2.add_collection(col)
ax2.set_title('PolyCollection using offsets')

plt.show()
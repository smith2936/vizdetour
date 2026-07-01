import matplotlib.pyplot as plt
import numpy as np
from matplotlib import collections

nverts = 60
ncurves = 20
offs = (0.1, 0.0)

yy = np.linspace(0, 2*np.pi, nverts)
ym = np.max(yy)
xx = (0.2 + (ym - yy) / ym) ** 2 * np.cos(yy - 0.4) * 0.5

rs = np.random.RandomState(19680801)

segs = []
for i in range(ncurves):
    xxx = xx + 0.02*rs.randn(nverts)
    curve = np.column_stack([xxx, yy * 100])
    segs.append(curve)

colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

fig, ax4 = plt.subplots()
col = collections.LineCollection(segs, offsets=offs, color=colors)
ax4.add_collection(col)
ax4.set_title('Successive data offsets')
ax4.set_xlabel('Zonal velocity component (m/s)')
ax4.set_ylabel('Depth (m)')
ax4.invert_yaxis()

plt.show()
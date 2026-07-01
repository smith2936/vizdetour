import matplotlib.pyplot as plt
import numpy as np

x, y = np.meshgrid(np.arange(7), np.arange(10))
z = np.sin(0.5 * x) * np.cos(0.52 * y)

mask = np.zeros_like(z, dtype=bool)
mask[2, 3:5] = True
mask[3:5, 4] = True
mask[7, 2] = True
mask[5, 0] = True
mask[0, 6] = True
z = np.ma.array(z, mask=mask)

fig, ax = plt.subplots()
cs = ax.contourf(x, y, z, corner_mask=False)
ax.contour(cs, colors='k')
ax.set_title('corner_mask=False')

ax.grid(c='k', ls='-', alpha=0.3)
ax.plot(np.ma.array(x, mask=~mask), y, 'ro')

plt.show()
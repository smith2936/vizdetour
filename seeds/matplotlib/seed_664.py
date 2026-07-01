import matplotlib.pyplot as plt
import numpy as np

nrows = 3
ncols = 5
Z = np.arange(nrows * ncols).reshape(nrows, ncols)

fig, axs = plt.subplots(2, 1, layout='constrained')

x = np.arange(ncols)
y = np.arange(nrows)
ax = axs[0]
ax.pcolormesh(x, y, Z, shading='auto', vmin=Z.min(), vmax=Z.max())
X, Y = np.meshgrid(x, y)
ax.plot(X.flat, Y.flat, 'o', color='m')
ax.set_xlim(-0.7, 5.2)
ax.set_ylim(-0.7, 3.2)
ax.set_title("shading='auto'; X, Y, Z: same shape (nearest)")

x = np.arange(ncols + 1)
y = np.arange(nrows + 1)
ax = axs[1]
ax.pcolormesh(x, y, Z, shading='auto', vmin=Z.min(), vmax=Z.max())
X, Y = np.meshgrid(x, y)
ax.plot(X.flat, Y.flat, 'o', color='m')
ax.set_xlim(-0.7, 5.2)
ax.set_ylim(-0.7, 3.2)
ax.set_title("shading='auto'; X, Y one larger than Z (flat)")

plt.show()
import matplotlib.pyplot as plt
import numpy as np

delta = 0.025

x = y = np.arange(-3.0, 3.01, delta)
X, Y = np.meshgrid(x, y)
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
Z = (Z1 - Z2) * 2

nr, nc = Z.shape

Z[-nr // 6:, -nc // 6:] = np.nan

Z = np.ma.array(Z)

Z[:nr // 6, :nc // 6] = np.ma.masked

interior = np.sqrt(X**2 + Y**2) < 0.5
Z[interior] = np.ma.masked

fig1, ax2 = plt.subplots(layout='constrained')
CS = ax2.contourf(X, Y, Z, 10, cmap="bone")

CS2 = ax2.contour(CS, levels=CS.levels[::2], colors='r')

ax2.set_title('Nonsense (3 masked regions)')
ax2.set_xlabel('word length anomaly')
ax2.set_ylabel('sentence length anomaly')

cbar = fig1.colorbar(CS)
cbar.ax.set_ylabel('verbosity coefficient')

cbar.add_lines(CS2)

plt.show()
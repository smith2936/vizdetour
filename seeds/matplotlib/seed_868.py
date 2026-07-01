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

fig2, ax2 = plt.subplots(layout='constrained')
levels = [-1.5, -1, -0.5, 0, 0.5, 1]
CS3 = ax2.contourf(X, Y, Z, levels, colors=('r', 'g', 'b'), extend='both')

CS3.cmap.set_under('yellow')
CS3.cmap.set_over('cyan')

CS4 = ax2.contour(X, Y, Z, levels, colors=('k',), linewidths=(3,))
ax2.set_title('Listed colors (3 masked regions)')
ax2.clabel(CS4, fmt='%2.1f', colors='w', fontsize=14)

fig2.colorbar(CS3)

plt.show()
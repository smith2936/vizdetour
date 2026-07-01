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

extends = ["neither", "both", "min", "max"]
cmap = plt.colormaps["winter"].with_extremes(under="magenta", over="yellow")

fig, axs = plt.subplots(2, 2, layout="constrained")

levels = [-1.5, -1, -0.5, 0, 0.5, 1]

for ax, extend in zip(axs.flat, extends):
    cs = ax.contourf(X, Y, Z, levels, cmap=cmap, extend=extend)
    fig.colorbar(cs, ax=ax, shrink=0.9)
    ax.set_title("extend = %s" % extend)
    ax.locator_params(nbins=4)

plt.show()
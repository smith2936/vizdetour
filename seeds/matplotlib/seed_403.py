import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as colors

N = 100

X, Y = np.mgrid[-3:3:complex(0, N), -2:2:complex(0, N)]
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
Z = (5 * Z1 - Z2) * 2

fig, ax = plt.subplots(3, 1, layout='constrained')

pcm = ax[0].pcolormesh(X, Y, Z, cmap='RdBu_r', shading='nearest',
                       vmin=-np.max(Z))
fig.colorbar(pcm, ax=ax[0], extend='both', orientation='vertical',
             label='linear scaling')


bounds = np.linspace(-2, 2, 11)
norm = colors.BoundaryNorm(boundaries=bounds, ncolors=256)
pcm = ax[1].pcolormesh(X, Y, Z, cmap='RdBu_r', shading='nearest',
                       norm=norm)
fig.colorbar(pcm, ax=ax[1], extend='both', orientation='vertical',
             label='BoundaryNorm\nlinspace(-2, 2, 11)')


bounds = np.array([-1, -0.5, 0, 2.5, 5])
norm = colors.BoundaryNorm(boundaries=bounds, ncolors=256)
pcm = ax[2].pcolormesh(X, Y, Z, cmap='RdBu_r', shading='nearest',
                       norm=norm)
fig.colorbar(pcm, ax=ax[2], extend='both', orientation='vertical',
             label='BoundaryNorm\n[-1, -0.5, 0, 2.5, 5]')

plt.show()
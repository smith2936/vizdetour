import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as colors

N = 100

X, Y = np.mgrid[-3:3:complex(0, N), -2:2:complex(0, N)]
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
Z = (5 * Z1 - Z2) * 2

fig, ax = plt.subplots(2, 1)

pcm = ax[0].pcolormesh(X, Y, Z, cmap='RdBu_r', shading='nearest',
                       vmin=-np.max(Z))
fig.colorbar(pcm, ax=ax[0], extend='both', label='linear scaling')

pcm = ax[1].pcolormesh(X, Y, Z, cmap='RdBu_r', shading='nearest',
                       norm=colors.SymLogNorm(linthresh=0.015,
                                              vmin=-10.0, vmax=10.0, base=10))
fig.colorbar(pcm, ax=ax[1], extend='both', label='SymLogNorm')

plt.show()
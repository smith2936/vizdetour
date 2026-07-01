import matplotlib.pyplot as plt
import numpy as np

# Recreate alarge and a for extension example
N = 450
x = np.arange(N) / N - 0.5
y = np.arange(N) / N - 0.5
aa = np.ones((N, N))
aa[::2, :] = -1

X, Y = np.meshgrid(x, y)
R = np.sqrt(X**2 + Y**2)
f0 = 5
k = 100
a = np.sin(np.pi * 2 * (f0 * R + k * R**2 / 2))

a[:int(N / 2), :][R[:int(N / 2), :] < 0.4] = -1
a[:int(N / 2), :][R[:int(N / 2), :] < 0.3] = 1
aa[:, int(N / 3):] = a[:, int(N / 3):]
alarge = aa

a = alarge + 1
cmap = plt.get_cmap('RdBu_r')
cmap.set_under('yellow')
cmap.set_over('limegreen')

fig, axs = plt.subplots(1, 3, figsize=(7, 3), layout='constrained')
for ax, interp, space in zip(axs.flat,
                             ['hanning', 'nearest', 'hanning'],
                             ['data', 'data', 'rgba']):
    im = ax.imshow(a, interpolation=interp, interpolation_stage=space,
                   cmap=cmap, vmin=0, vmax=2)
    title = f"interpolation='{interp}'\nstage='{space}'"
    if ax == axs[2]:
        title += '\nDefault'
    ax.set_title(title, fontsize='medium')
fig.colorbar(im, ax=axs, extend='both', shrink=0.8)

plt.show()
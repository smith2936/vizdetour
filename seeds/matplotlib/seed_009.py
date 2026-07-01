import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(19680801)
xdata = rng.normal(size=1000)

fig, ax = plt.subplots(layout='constrained', figsize=(3.5, 3))

for nn, dx in enumerate([0.1, 0.4, 1.2]):
    xbins = np.arange(-4, 4, dx)
    ax.hist(xdata, bins=xbins, weights=1/len(xdata) * np.ones(len(xdata)),
                   histtype='step', label=f'{dx}')
ax.set_xlabel('x bins [$V$]')
ax.set_ylabel('Bin count / N')
ax.legend(fontsize='small', title='bin width:')

plt.show()
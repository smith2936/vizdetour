import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(19680801)
xdata = rng.normal(size=1000)
xpdf = np.arange(-4, 4, 0.1)
pdf = 1 / (np.sqrt(2 * np.pi)) * np.exp(-xpdf**2 / 2)

fig, ax = plt.subplot_mosaic([['False', 'True']], layout='constrained')

ax['True'].plot(xpdf, pdf, '--', label='$f_X(x)$', color='k')

for nn, dx in enumerate([0.1, 0.4, 1.2]):
    xbins = np.arange(-4, 4, dx)
    ax['False'].plot(xpdf, pdf*1000*dx, '--', color=f'C{nn}')
    ax['False'].hist(xdata, bins=xbins, density=False, histtype='step')
    ax['True'].hist(xdata, bins=xbins, density=True, histtype='step', label=dx)

ax['False'].set_xlabel('x bins [$V$]')
ax['False'].set_ylabel('Count per bin')
ax['True'].set_ylabel('Probability density [$V^{-1}$]')
ax['True'].set_xlabel('x bins [$V$]')
ax['True'].legend(fontsize='small', title='bin width:')

plt.show()
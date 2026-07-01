import matplotlib.pyplot as plt
import numpy as np

x4 = [8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8]
y4 = [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89]

fig, ax = plt.subplots(figsize=(6, 6))
ax.set(xlim=(0, 20), ylim=(2, 14))
ax.set(xticks=(0, 10, 20), yticks=(4, 8, 12))

label = 'IV'
ax.text(0.1, 0.9, label, fontsize=20, transform=ax.transAxes, va='top')
ax.tick_params(direction='in', top=True, right=True)
ax.plot(x4, y4, 'o')

p1, p0 = np.polyfit(x4, y4, deg=1)
ax.axline(xy1=(0, p0), slope=p1, color='r', lw=2)

stats = (f'$\\mu$ = {np.mean(y4):.2f}\n'
         f'$\\sigma$ = {np.std(y4):.2f}\n'
         f'$r$ = {np.corrcoef(x4, y4)[0][1]:.2f}')
bbox = dict(boxstyle='round', fc='blanchedalmond', ec='orange', alpha=0.5)
ax.text(0.95, 0.07, stats, fontsize=9, bbox=bbox,
        transform=ax.transAxes, horizontalalignment='right')

plt.show()
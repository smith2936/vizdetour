import matplotlib.pyplot as plt
import numpy as np

x = [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5]
y2 = [9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74]

fig, ax = plt.subplots(figsize=(6, 6))
ax.set(xlim=(0, 20), ylim=(2, 14))
ax.set(xticks=(0, 10, 20), yticks=(4, 8, 12))

label = 'II'
ax.text(0.1, 0.9, label, fontsize=20, transform=ax.transAxes, va='top')
ax.tick_params(direction='in', top=True, right=True)
ax.plot(x, y2, 'o')

p1, p0 = np.polyfit(x, y2, deg=1)
ax.axline(xy1=(0, p0), slope=p1, color='r', lw=2)

stats = (f'$\\mu$ = {np.mean(y2):.2f}\n'
         f'$\\sigma$ = {np.std(y2):.2f}\n'
         f'$r$ = {np.corrcoef(x, y2)[0][1]:.2f}')
bbox = dict(boxstyle='round', fc='blanchedalmond', ec='orange', alpha=0.5)
ax.text(0.95, 0.07, stats, fontsize=9, bbox=bbox,
        transform=ax.transAxes, horizontalalignment='right')

plt.show()
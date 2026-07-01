import matplotlib.pyplot as plt
import numpy as np

x = [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5]
y1 = [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]

fig, ax = plt.subplots(figsize=(6, 6))
ax.set(xlim=(0, 20), ylim=(2, 14))
ax.set(xticks=(0, 10, 20), yticks=(4, 8, 12))

label = 'I'
ax.text(0.1, 0.9, label, fontsize=20, transform=ax.transAxes, va='top')
ax.tick_params(direction='in', top=True, right=True)
ax.plot(x, y1, 'o')

p1, p0 = np.polyfit(x, y1, deg=1)
ax.axline(xy1=(0, p0), slope=p1, color='r', lw=2)

stats = (f'$\\mu$ = {np.mean(y1):.2f}\n'
         f'$\\sigma$ = {np.std(y1):.2f}\n'
         f'$r$ = {np.corrcoef(x, y1)[0][1]:.2f}')
bbox = dict(boxstyle='round', fc='blanchedalmond', ec='orange', alpha=0.5)
ax.text(0.95, 0.07, stats, fontsize=9, bbox=bbox,
        transform=ax.transAxes, horizontalalignment='right')

plt.show()
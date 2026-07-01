import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

fig, (ax1, ax2) = plt.subplots(1, 2)

ax1.add_patch(Rectangle((0.1, 0.5), 0.8, 0.3, hatch=".", hatchcolor='red',
                        edgecolor='black', lw=2))

ax1.add_patch(Rectangle((0.1, 0.1), 0.8, 0.3, hatch='x', edgecolor='orange', lw=2))

x = range(1, 5)
y = range(1, 5)

ax2.bar(x, y, facecolor='none', edgecolor='red', hatch='//', hatchcolor='blue')
ax2.set_xlim(0, 5)
ax2.set_ylim(0, 5)

plt.show()
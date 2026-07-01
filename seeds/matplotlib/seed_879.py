import matplotlib.pyplot as plt
import numpy as np


def adjust_spines(ax, visible_spines):
    ax.label_outer(remove_inner_ticks=True)
    ax.grid(color='0.9')

    for loc, spine in ax.spines.items():
        if loc in visible_spines:
            spine.set_position(('outward', 10))  
        else:
            spine.set_visible(False)


x = np.linspace(0, 2 * np.pi, 100)

fig, ax = plt.subplots()
ax.plot(x, np.cos(x))
adjust_spines(ax, [])

plt.show()
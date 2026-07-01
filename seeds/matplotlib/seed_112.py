import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

def setup(ax, title):
    ax.yaxis.set_major_locator(ticker.NullLocator())
    ax.spines[['left', 'right', 'top']].set_visible(False)
    ax.xaxis.set_ticks_position('bottom')
    ax.tick_params(which='major', width=1.00, length=5)
    ax.tick_params(which='minor', width=0.75, length=2.5)
    ax.set_xlim(0, 5)
    ax.set_ylim(0, 1)
    ax.text(0.0, 0.2, title, transform=ax.transAxes,
            fontsize=14, fontname='Monospace', color='tab:blue')

fig, ax = plt.subplots(figsize=(8, 1))
setup(ax, title="FixedLocator([0, 1, 5])")
ax.xaxis.set_major_locator(ticker.FixedLocator([0, 1, 5]))
ax.xaxis.set_minor_locator(ticker.FixedLocator(np.linspace(0.2, 0.8, 4)))

plt.tight_layout()
plt.show()
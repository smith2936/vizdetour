import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

def setup(ax, title):
    ax.spines[['left', 'right', 'top']].set_visible(False)
    ax.xaxis.set_ticks_position('bottom')
    ax.tick_params(which='major', width=1.00, length=5)
    ax.tick_params(which='minor', width=0.75, length=2.5)
    ax.set_xscale('log')
    ax.set_xlim(10**3, 10**10)
    ax.set_ylim(0, 1)
    ax.text(0.0, 0.2, title, transform=ax.transAxes,
            fontsize=14, fontname='Monospace', color='tab:blue')

fig, ax = plt.subplots(figsize=(8, 1))
setup(ax, title="LogLocator(base=10, numticks=15)")
ax.xaxis.set_major_locator(ticker.LogLocator(base=10, numticks=15))

plt.tight_layout()
plt.show()
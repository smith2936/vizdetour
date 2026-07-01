import matplotlib.pyplot as plt
import numpy as np
from matplotlib.dates import (AutoDateFormatter, ConciseDateFormatter, DateFormatter)
import matplotlib.ticker as ticker


def plot_axis(ax, locator=None, xmax='2002-02-01', fmt=None, formatter=None):
    ax.spines[['left', 'right', 'top']].set_visible(False)
    ax.yaxis.set_major_locator(ticker.NullLocator())
    ax.tick_params(which='major', width=1.00, length=5)
    ax.tick_params(which='minor', width=0.75, length=2.5)
    ax.set_xlim(np.datetime64('2000-02-01'), np.datetime64(xmax))
    if locator:
        ax.xaxis.set_major_locator(eval(locator))
        ax.xaxis.set_major_formatter(DateFormatter(fmt))
    else:
        ax.xaxis.set_major_formatter(eval(formatter))
    ax.text(0.0, 0.2, locator or formatter, transform=ax.transAxes,
            fontsize=14, fontname='Monospace', color='tab:blue')


formatters = [
    'AutoDateFormatter(ax.xaxis.get_major_locator())',
    'ConciseDateFormatter(ax.xaxis.get_major_locator())',
    'DateFormatter("%b %Y")',
]

fig, axs = plt.subplots(len(formatters), 1, figsize=(8, len(formatters) * 0.8),
                        layout='constrained')
fig.suptitle('Date Formatters')
for ax, fmt in zip(axs, formatters):
    plot_axis(ax, formatter=fmt)

plt.show()
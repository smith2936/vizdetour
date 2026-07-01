import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
import matplotlib as mpl
from matplotlib import cycler

np.random.seed(19680801)

N = 10
data = (np.geomspace(1, 10, 100) + np.random.randn(N, 100)).T
cmap = plt.colormaps["coolwarm"]
mpl.rcParams['axes.prop_cycle'] = cycler(color=cmap(np.linspace(0, 1, N)))

custom_lines = [Line2D([0], [0], color=cmap(0.), lw=4),
                Line2D([0], [0], color=cmap(.5), lw=4),
                Line2D([0], [0], color=cmap(1.), lw=4)]

fig, ax = plt.subplots()
lines = ax.plot(data)
ax.legend(custom_lines, ['Cold', 'Medium', 'Hot'])
plt.show()
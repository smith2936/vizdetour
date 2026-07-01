import matplotlib.pyplot as plt
import numpy as np


def color_cycle_example(ax):
    L = 6
    x = np.linspace(0, L)
    ncolors = len(plt.rcParams['axes.prop_cycle'])
    shift = np.linspace(0, L, ncolors, endpoint=False)
    for s in shift:
        ax.plot(x, np.sin(x + s), 'o-')


plt.style.use('grayscale')

fig, ax = plt.subplots()
color_cycle_example(ax)
plt.show()
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')

L = 2*np.pi
x = np.linspace(0, L)
ncolors = len(plt.rcParams['axes.prop_cycle'])
shift = np.linspace(0, L, ncolors, endpoint=False)

fig, ax2 = plt.subplots()
for s in shift:
    ax2.plot(x, np.sin(x + s), '-')
ax2.margins(0)

plt.show()
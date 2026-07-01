import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from matplotlib import cycler

np.random.seed(19680801)

N = 10
data = (np.geomspace(1, 10, 100) + np.random.randn(N, 100)).T
cmap = plt.colormaps["coolwarm"]
mpl.rcParams['axes.prop_cycle'] = cycler(color=cmap(np.linspace(0, 1, N)))

fig, ax = plt.subplots()
lines = ax.plot(data)
plt.show()
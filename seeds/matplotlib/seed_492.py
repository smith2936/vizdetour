import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)

n_bins = 10
x = np.random.randn(1000, 3)

fig, ax = plt.subplots()

facecolors = ['green', 'red', 'blue']

ax.hist(x, n_bins, histtype="barstacked", facecolor=facecolors, label=facecolors)
ax.legend()
ax.set_title("Bars with different Facecolors")

plt.show()
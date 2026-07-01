import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)

n_bins = 10
x = np.random.randn(1000, 3)

fig, ax = plt.subplots()

edgecolors = ['green', 'red', 'blue']

ax.hist(x, n_bins, fill=False, histtype="step", stacked=True,
        edgecolor=edgecolors, label=edgecolors)
ax.legend()
ax.set_title('Stacked Steps with Edgecolors')

plt.show()
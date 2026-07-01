import matplotlib.pyplot as plt
import numpy as np
from numpy.random import multivariate_normal
import matplotlib.colors as mcolors

np.random.seed(19680801)

data = np.vstack([
    multivariate_normal([10, 10], [[3, 2], [2, 3]], size=100000),
    multivariate_normal([30, 20], [[3, 1], [1, 3]], size=1000)
])

fig, ax = plt.subplots()
ax.set_title('Linear normalization')
ax.hist2d(data[:, 0], data[:, 1], bins=100)

plt.tight_layout()
plt.show()
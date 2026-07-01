import matplotlib.pyplot as plt
import numpy as np

N = 450
x = np.arange(N) / N - 0.5
y = np.arange(N) / N - 0.5
aa = np.ones((N, N))
aa[::2, :] = -1

fig = plt.figure(figsize=(2, 2))
ax = fig.add_axes((0, 0, 1, 1))
ax.imshow(aa[:400, :400], cmap='RdBu_r', interpolation='nearest')

plt.show()
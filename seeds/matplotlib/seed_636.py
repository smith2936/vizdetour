import matplotlib.pyplot as plt
import numpy as np

fig, ax1 = plt.subplots(figsize=(3.5, 3))

np.random.seed(19680801)
s = 2.9 * np.convolve(np.random.randn(500), np.ones(30) / 30, mode='valid')
ax1.plot(s)
ax1.axhspan(-1, 1, alpha=0.1)
ax1.set(ylim=(-1.5, 1.5), title="axhspan")

plt.show()
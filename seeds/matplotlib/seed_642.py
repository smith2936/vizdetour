import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors

N_points = 100000

rng = np.random.default_rng(19680801)
dist1 = rng.standard_normal(N_points)
dist2 = 0.4 * rng.standard_normal(N_points) + 5

fig, axs = plt.subplots(3, 1, figsize=(5, 15), sharex=True, sharey=True, tight_layout=True)

axs[0].hist2d(dist1, dist2, bins=40)
axs[1].hist2d(dist1, dist2, bins=40, norm=colors.LogNorm())
axs[2].hist2d(dist1, dist2, bins=(80, 10), norm=colors.LogNorm())

plt.show()
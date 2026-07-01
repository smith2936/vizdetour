import matplotlib.pyplot as plt
import numpy as np

N_points = 100000
n_bins = 20

rng = np.random.default_rng(19680801)
dist1 = rng.standard_normal(N_points)
dist2 = 0.4 * rng.standard_normal(N_points) + 5

fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True)

axs[0].hist(dist1, bins=n_bins)
axs[1].hist(dist2, bins=n_bins)

plt.show()
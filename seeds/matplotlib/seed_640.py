import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter

N_points = 100000
n_bins = 20

rng = np.random.default_rng(19680801)
dist1 = rng.standard_normal(N_points)

fig, axs = plt.subplots(1, 2, tight_layout=True)

N, bins, patches = axs[0].hist(dist1, bins=n_bins)

fracs = N / N.max()
norm = colors.Normalize(fracs.min(), fracs.max())

for thisfrac, thispatch in zip(fracs, patches):
    color = plt.colormaps["viridis"](norm(thisfrac))
    thispatch.set_facecolor(color)

axs[1].hist(dist1, bins=n_bins, density=True)
axs[1].yaxis.set_major_formatter(PercentFormatter(xmax=1))

plt.show()
import matplotlib.pyplot as plt
import numpy as np

N_points = 100000

rng = np.random.default_rng(19680801)
dist1 = rng.standard_normal(N_points)
dist2 = 0.4 * rng.standard_normal(N_points) + 5

fig, ax = plt.subplots(tight_layout=True)
hist = ax.hist2d(dist1, dist2)

plt.show()
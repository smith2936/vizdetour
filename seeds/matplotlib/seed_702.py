import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(seed=19680801)

fig, ax = plt.subplots()

data = rng.standard_normal((250, 250))
data = np.clip(data, -1, 1)

cax = ax.imshow(data, cmap='afmhot')
ax.set_title('Gaussian noise with horizontal colorbar')

cbar = fig.colorbar(cax, orientation='horizontal')
cbar.set_ticks(ticks=[-1, 0, 1], labels=['Low', 'Medium', 'High'])

plt.show()
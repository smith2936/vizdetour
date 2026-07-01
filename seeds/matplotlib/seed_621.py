import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)

mu_x = 200
sigma_x = 25
x = np.random.normal(mu_x, sigma_x, size=100)

bins = [100, 150, 180, 195, 205, 220, 250, 300]

fig, ax = plt.subplots()

ax.hist(x, bins, density=True, histtype='bar', rwidth=0.8)
ax.set_title('bar, unequal bins')

plt.show()
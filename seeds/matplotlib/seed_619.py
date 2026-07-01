import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)

mu_x = 200
sigma_x = 25
x = np.random.normal(mu_x, sigma_x, size=100)

fig, ax = plt.subplots()

ax.hist(x, 20, density=True, histtype='step', facecolor='g',
        alpha=0.75)
ax.set_title('step')

plt.show()
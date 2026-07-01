import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)

mu_x = 200
sigma_x = 25
x = np.random.normal(mu_x, sigma_x, size=100)

mu_w = 200
sigma_w = 10
w = np.random.normal(mu_w, sigma_w, size=100)

fig, ax = plt.subplots()

ax.hist(x, density=True, histtype='barstacked', rwidth=0.8)
ax.hist(w, density=True, histtype='barstacked', rwidth=0.8)
ax.set_title('barstacked')

plt.show()
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)

mu = 200
sigma = 25
n_bins = 25
data = np.random.normal(mu, sigma, size=100)

fig, ax = plt.subplots(figsize=(6, 4), layout="constrained")

ax.ecdf(data, complementary=True, label="CCDF")
n, bins, patches = ax.hist(data, bins=25, density=True, histtype="step", cumulative=-1,
                          label="Reversed cumulative histogram")
x = np.linspace(data.min(), data.max())
y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
     np.exp(-0.5 * (1 / sigma * (x - mu))**2))
y = y.cumsum()
y /= y[-1]
ax.plot(x, 1 - y, "k--", linewidth=1.5, label="Theory")

fig.suptitle("Cumulative distributions - CCDF")
ax.grid(True)
ax.legend()
ax.set_xlabel("Annual rainfall (mm)")
ax.set_ylabel("Probability of occurrence")
ax.label_outer()

plt.show()
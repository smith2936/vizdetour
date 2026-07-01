import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)

def plot_scatter(ax, prng, nb_samples=100):
    for mu, sigma, marker in [(-.5, 0.75, 'o'), (0.75, 1., 's')]:
        x, y = prng.normal(loc=mu, scale=sigma, size=(2, nb_samples))
        ax.plot(x, y, ls='none', marker=marker)
    ax.set_xlabel('X-label')
    ax.set_title('Axes title')
    return ax


prng = np.random.RandomState(96917002)
fig, ax = plt.subplots()
plot_scatter(ax, prng)
plt.show()
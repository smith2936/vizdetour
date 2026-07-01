import matplotlib.pyplot as plt
import numpy as np

prng = np.random.RandomState(96917002)

def plot_bar_graphs(ax, prng, min_value=5, max_value=25, nb_samples=5):
    x = np.arange(nb_samples)
    ya, yb = prng.randint(min_value, max_value, size=(2, nb_samples))
    width = 0.25
    ax.bar(x, ya, width)
    ax.bar(x + width, yb, width, color='C2')
    ax.set_xticks(x + width, labels=['a', 'b', 'c', 'd', 'e'])
    return ax


fig, ax = plt.subplots()
plot_bar_graphs(ax, prng)
plt.show()
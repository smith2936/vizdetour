import matplotlib.pyplot as plt
import numpy as np

prng = np.random.RandomState(96917002)

def plot_colored_circles(ax, prng, nb_samples=15):
    for sty_dict, j in zip(plt.rcParams['axes.prop_cycle'](),
                           range(nb_samples)):
        ax.add_patch(plt.Circle(prng.normal(scale=3, size=2),
                                radius=1.0, color=sty_dict['color']))
    ax.grid(visible=True)

    plt.title('ax.grid(True)', family='monospace', fontsize='small')

    ax.set_xlim([-4, 8])
    ax.set_ylim([-5, 6])
    ax.set_aspect('equal', adjustable='box')  
    return ax


fig, ax = plt.subplots()
plot_colored_circles(ax, prng)
plt.show()
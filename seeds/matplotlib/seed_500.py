import matplotlib.pyplot as plt
import numpy as np

prng = np.random.RandomState(96917002)

def plot_image_and_patch(ax, prng, size=(20, 20)):
    values = prng.random_sample(size=size)
    ax.imshow(values, interpolation='none')
    c = plt.Circle((5, 5), radius=5, label='patch')
    ax.add_patch(c)
    
    ax.set_xticks([])
    ax.set_yticks([])


fig, ax = plt.subplots()
plot_image_and_patch(ax, prng)
plt.show()
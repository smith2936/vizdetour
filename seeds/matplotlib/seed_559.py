import matplotlib.pyplot as plt
import numpy as np


def image_and_patch_example(ax):
    ax.imshow(np.random.random(size=(20, 20)), interpolation='none')
    c = plt.Circle((5, 5), radius=5, label='patch')
    ax.add_patch(c)


plt.style.use('grayscale')

fig, ax = plt.subplots()
image_and_patch_example(ax)
plt.show()
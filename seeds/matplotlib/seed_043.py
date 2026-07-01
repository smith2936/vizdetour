import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
for pos in np.linspace(-2, 1, 10):
    ax.axline((pos, 0), slope=0.5, color='k', transform=ax.transAxes)

ax.set(xlim=(0, 1), ylim=(0, 1))
plt.show()
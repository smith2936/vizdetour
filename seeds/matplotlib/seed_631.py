import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse

angle_step = 45  
angles = np.arange(0, 180, angle_step)

fig, ax = plt.subplots()
ax.set(xlim=(-2.2, 2.2), ylim=(-2.2, 2.2), aspect="equal")

for angle in angles:
    ellipse = Ellipse((0, 0), 4, 2, angle=angle, alpha=0.1)
    ax.add_artist(ellipse)

plt.show()
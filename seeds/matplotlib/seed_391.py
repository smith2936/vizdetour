import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm

fig, ax = plt.subplots()

num_points_x = 10
num_points_y = 9
x = np.linspace(0, 1, num_points_x)
y = np.linspace(0, 1, num_points_y)

X, Y = np.meshgrid(x, y)
X[1::2, :] += (x[1] - x[0]) / 2  

colors = [cm.rainbow(val) for val in x]

ax.scatter(
    X.ravel(),
    Y.ravel(),
    s=1700,
    facecolor="none",
    edgecolor="gray",
    linewidth=2,
    marker="h",  
    hatch="xxx",
    hatchcolor=colors,
)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

plt.show()
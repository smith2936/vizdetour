import matplotlib.pyplot as plt
from matplotlib.contour import ContourSet

lines0 = [[[0, 0], [0, 4]]]
lines1 = [[[2, 0], [1, 2], [1, 3]]]
lines2 = [[[3, 0], [3, 2]], [[3, 3], [3, 4]]]  

filled01 = [[[0, 0], [0, 4], [1, 3], [1, 2], [2, 0]]]
filled12 = [[[2, 0], [3, 0], [3, 2], [1, 3], [1, 2]],   
            [[1, 4], [3, 4], [3, 3]]]

fig, ax = plt.subplots()

cs = ContourSet(ax, [0, 1, 2], [filled01, filled12], filled=True, cmap="bone")
cbar = fig.colorbar(cs)

lines = ContourSet(
    ax, [0, 1, 2], [lines0, lines1, lines2], cmap="cool", linewidths=3)
cbar.add_lines(lines)

ax.set(xlim=(-0.5, 3.5), ylim=(-0.5, 4.5),
       title='User-specified contours')

plt.show()
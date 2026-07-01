import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.axes_divider import make_axes_area_auto_adjustable

fig = plt.figure()
ax = fig.add_axes((0, 0, 1, 1))

ax.set_yticks([0.5], labels=["very long label"])

make_axes_area_auto_adjustable(ax)

plt.show()
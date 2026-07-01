from matplotlib import pyplot as plt
from matplotlib.patches import Circle
from matplotlib.offsetbox import AnchoredOffsetbox, DrawingArea


fig, ax = plt.subplots()
ax.set_aspect(1)

area = DrawingArea(width=40, height=20)
area.add_artist(Circle((10, 10), 10, fc="tab:blue"))
area.add_artist(Circle((30, 10), 5, fc="tab:red"))
box = AnchoredOffsetbox(
    child=area, loc="upper right", pad=0, frameon=False)
ax.add_artist(box)

plt.show()
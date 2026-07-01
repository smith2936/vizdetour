from matplotlib import pyplot as plt
from matplotlib.offsetbox import AnchoredOffsetbox, TextArea


fig, ax = plt.subplots()
ax.set_aspect(1)

box = AnchoredOffsetbox(child=TextArea("Figure 1a"),
                        loc="upper left", frameon=True)
box.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
ax.add_artist(box)

plt.show()
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnnotationBbox, TextArea

fig, ax = plt.subplots()

xy = (0.5, 0.7)
ax.plot(xy[0], xy[1], ".r")

offsetbox = TextArea("Test")

ab = AnnotationBbox(offsetbox, xy,
                    xybox=(1.02, xy[1]),
                    xycoords='data',
                    boxcoords=("axes fraction", "data"),
                    box_alignment=(0., 0.5),
                    arrowprops=dict(arrowstyle="->"))
ax.add_artist(ab)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

plt.show()
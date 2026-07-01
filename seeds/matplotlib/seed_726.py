import matplotlib.pyplot as plt
import numpy as np

from matplotlib.cbook import get_sample_data
from matplotlib.offsetbox import AnnotationBbox, DrawingArea, OffsetImage, TextArea
from matplotlib.patches import Circle

fig, ax = plt.subplots()

xy = (0.5, 0.7)
ax.plot(xy[0], xy[1], ".r")

offsetbox = TextArea("Test 1")

ab = AnnotationBbox(offsetbox, xy,
                    xybox=(-20, 40),
                    xycoords='data',
                    boxcoords="offset points",
                    arrowprops=dict(arrowstyle="->"),
                    bboxprops=dict(boxstyle="sawtooth"))
ax.add_artist(ab)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

plt.show()
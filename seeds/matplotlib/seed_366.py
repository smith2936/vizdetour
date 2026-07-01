import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm
from mpl_toolkits.axes_grid1.anchored_artists import AnchoredDirectionArrows

np.random.seed(19680801)

fig, ax = plt.subplots()
ax.imshow(np.random.random((10, 10)))

fontprops = fm.FontProperties(family='serif')

rotated_arrow = AnchoredDirectionArrows(
    ax.transAxes,
    '30', '120',
    loc='center',
    color='w',
    angle=30,
    fontproperties=fontprops
)
ax.add_artist(rotated_arrow)

plt.show()
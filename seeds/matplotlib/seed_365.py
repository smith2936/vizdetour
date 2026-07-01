import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1.anchored_artists import AnchoredDirectionArrows

np.random.seed(19680801)

fig, ax = plt.subplots()
ax.imshow(np.random.random((10, 10)))

high_contrast_part_1 = AnchoredDirectionArrows(
    ax.transAxes,
    '111', r'11$\overline{2}$',
    loc='upper right',
    arrow_props={'ec': 'w', 'fc': 'none', 'alpha': 1, 'lw': 2}
)
ax.add_artist(high_contrast_part_1)

high_contrast_part_2 = AnchoredDirectionArrows(
    ax.transAxes,
    '111', r'11$\overline{2}$',
    loc='upper right',
    arrow_props={'ec': 'none', 'fc': 'k'},
    text_props={'ec': 'w', 'fc': 'k', 'lw': 0.4}
)
ax.add_artist(high_contrast_part_2)

plt.show()
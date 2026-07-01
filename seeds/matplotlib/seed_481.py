import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse, Polygon

x = np.arange(0, 40, 0.2)
y2 = np.ones(x.shape) * 4

fig, ax = plt.subplots()
ax.fill_between(x, np.sin(x) * 4 + 30, y2=0,
                hatch='///', zorder=2, fc='c')
ax.add_patch(Ellipse((4, 50), 10, 10, fill=True,
                     hatch='*', facecolor='y'))
ax.add_patch(Polygon([(10, 20), (30, 50), (50, 10)],
                     hatch='\\/...', facecolor='g'))
ax.set_xlim(0, 40)
ax.set_ylim(10, 60)
ax.set_aspect(1)

plt.show()
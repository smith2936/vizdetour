import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse

el = Ellipse((0, 0), 10, 20, facecolor='r', alpha=0.5)

fig, ax = plt.subplots(subplot_kw=dict(aspect='equal'))
ax.add_artist(el)
el.set_clip_box(ax.bbox)
ax.annotate('the top',
            xy=(np.pi/2., 10.),      
            xytext=(np.pi/3, 20.),   
            xycoords='polar',
            textcoords='polar',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='left',
            verticalalignment='bottom',
            clip_on=True)  

ax.set(xlim=[-20, 20], ylim=[-20, 20])

plt.show()
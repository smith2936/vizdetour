import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')

fig, ax4 = plt.subplots()
for i, color in enumerate(plt.rcParams['axes.prop_cycle']):
    xy = np.random.normal(size=2)
    ax4.add_patch(plt.Circle(xy, radius=0.3, color=color['color']))
ax4.axis('equal')
ax4.margins(0)

plt.show()
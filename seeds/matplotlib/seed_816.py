import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import axisartist

fig = plt.figure(figsize=(6, 3), layout="constrained")
gs = fig.add_gridspec(1, 2)

ax0 = fig.add_subplot(gs[0, 0], axes_class=axisartist.Axes)
ax0.axis["y=0"] = ax0.new_floating_axis(nth_coord=0, value=0, axis_direction="bottom")
ax0.axis["y=0"].toggle(all=True)
ax0.axis["y=0"].label.set_text("y = 0")
ax0.axis["bottom", "top", "right"].set_visible(False)

x = np.arange(0, 2*np.pi, 0.01)
ax0.plot(x, np.sin(x))

plt.show()
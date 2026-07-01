import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import axisartist

fig = plt.figure(figsize=(6, 3), layout="constrained")
gs = fig.add_gridspec(1, 2)

ax1 = fig.add_subplot(gs[0, 1], axes_class=axisartist.axislines.AxesZero)
ax1.axis["xzero"].set_visible(True)
ax1.axis["xzero"].label.set_text("Axis Zero")
ax1.axis["bottom", "top", "right"].set_visible(False)

x = np.arange(0, 2*np.pi, 0.01)
ax1.plot(x, np.sin(x))

plt.show()
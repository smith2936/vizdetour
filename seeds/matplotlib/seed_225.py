import matplotlib.pyplot as plt
import numpy as np
from matplotlib.image import NonUniformImage

x = np.linspace(-4, 4, 9)
y = np.linspace(-4, 4, 9)
z = np.sqrt(x[np.newaxis, :]**2 + y[:, np.newaxis]**2)

fig, ax = plt.subplots(layout='constrained')
interp = 'bilinear'
im = NonUniformImage(ax, interpolation=interp, extent=(-4, 4, -4, 4), cmap="Purples")
im.set_data(x, y, z)
ax.add_image(im)
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
ax.set_title(interp)
plt.show()
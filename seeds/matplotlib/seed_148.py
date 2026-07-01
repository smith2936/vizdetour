import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LightSource


y, x = np.mgrid[-4:2:200j, -4:2:200j]
z = 10 * np.cos(x**2 + y**2)

cmap = plt.colormaps["copper"]
ls = LightSource(315, 45)
rgb = ls.shade(z, cmap)

fig, ax = plt.subplots()
ax.imshow(rgb, interpolation='bilinear')

im = ax.imshow(z, cmap=cmap)
im.remove()
fig.colorbar(im, ax=ax)

ax.set_title('Using a colorbar with a shaded plot', size='x-large')
plt.show()
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LightSource, Normalize


y, x = np.mgrid[-4:2:200j, -4:2:200j]
z1 = np.sin(x**2)  
z2 = np.cos(x**2 + y**2)  

norm = Normalize(z2.min(), z2.max())
cmap = plt.colormaps["RdBu"]

ls = LightSource(315, 45)
rgb = ls.shade_rgb(cmap(norm(z2)), z1)

fig, ax = plt.subplots()
ax.imshow(rgb, interpolation='bilinear')
ax.set_title('Shade by one variable, color by another', size='x-large')
plt.show()
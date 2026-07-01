import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LightSource


y, x = np.mgrid[-4:2:200j, -4:2:200j]
z = 10 * np.cos(x**2 + y**2)

z[100, 105] = 2000
z[120, 110] = -9000

ls = LightSource(315, 45)
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(8, 4.5))

rgb = ls.shade(z, plt.colormaps["copper"])
ax1.imshow(rgb, interpolation='bilinear')
ax1.set_title('Full range of data')

rgb = ls.shade(z, plt.colormaps["copper"], vmin=-10, vmax=10)
ax2.imshow(rgb, interpolation='bilinear')
ax2.set_title('Manually set range')

fig.suptitle('Avoiding Outliers in Shaded Plots', size='x-large')
plt.show()
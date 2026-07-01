import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as colors

x0, x1 = -5, 5
y0, y1 = -3, 3
x = np.linspace(x0, x1, 500)
y = np.linspace(y0, y1, 500)
X, Y = np.meshgrid(x, y)
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
Z = (Z1 - Z2) * 2

palette = plt.colormaps["gray"].with_extremes(over='r', under='g', bad='b')
Zm = np.ma.masked_where(Z > 1.2, Z)

fig, ax2 = plt.subplots(figsize=(6, 2.7))

im = ax2.imshow(Zm, interpolation='nearest',
                cmap=palette,
                norm=colors.BoundaryNorm([-1, -0.5, -0.2, 0, 0.2, 0.5, 1],
                                         ncolors=palette.N),
                aspect='auto',
                origin='lower',
                extent=[x0, x1, y0, y1])
ax2.set_title('With BoundaryNorm')
cbar = fig.colorbar(im, extend='both', spacing='proportional',
                    shrink=0.9, ax=ax2)
cbar.set_label('proportional')

plt.suptitle('imshow, with out-of-range and masked data - Plot 2')
plt.show()
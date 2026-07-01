import matplotlib.pyplot as plt
from matplotlib import cbook
from mpl_toolkits.axes_grid1 import ImageGrid

fig = plt.figure(figsize=(10.5, 2.5))
Z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")  
extent = (-3, 4, -4, 3)

grid = ImageGrid(
    fig, 142,  
    nrows_ncols=(2, 2), axes_pad=0.0, label_mode="L", share_all=True,
    cbar_location="top", cbar_mode="single")
for ax in grid:
    im = ax.imshow(Z, extent=extent)
grid.cbar_axes[0].colorbar(im)
for cax in grid.cbar_axes:
    cax.tick_params(labeltop=False)

grid.axes_llc.set(xticks=[-2, 0, 2], yticks=[-2, 0, 2])

plt.show()
import matplotlib.pyplot as plt
from matplotlib import cbook
from mpl_toolkits.axes_grid1 import ImageGrid

fig = plt.figure(figsize=(10.5, 2.5))
Z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")  
extent = (-3, 4, -4, 3)

grid = ImageGrid(
    fig, 141,  
     nrows_ncols=(2, 2), axes_pad=0.05, label_mode="1")
for ax in grid:
    ax.imshow(Z, extent=extent)

grid.axes_llc.set(xticks=[-2, 0, 2], yticks=[-2, 0, 2])

plt.show()
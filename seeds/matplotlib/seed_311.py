import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import inset_locator

fig, ax1 = plt.subplots(figsize=[3, 3])

im1 = ax1.imshow([[1, 2], [2, 3]])
axins1 = inset_locator.inset_axes(
    ax1,
    width="50%",  
    height="5%",  
    loc="upper right",
)
axins1.xaxis.set_ticks_position("bottom")
fig.colorbar(im1, cax=axins1, orientation="horizontal", ticks=[1, 2, 3])

plt.show()
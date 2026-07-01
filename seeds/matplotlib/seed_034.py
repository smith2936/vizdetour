import matplotlib.pyplot as plt
from matplotlib import cbook


def get_demo_image():
    z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")  
    return z, (-3, 4, -4, 3)


def demo_locatable_axes_hard():
    from mpl_toolkits.axes_grid1 import Size, SubplotDivider

    fig = plt.figure(figsize=(6, 6))
    divider = SubplotDivider(fig, 2, 2, 2, aspect=True)

    ax = fig.add_subplot(axes_locator=divider.new_locator(nx=0, ny=0))
    ax_cb = fig.add_subplot(axes_locator=divider.new_locator(nx=2, ny=0))

    divider.set_horizontal([
        Size.AxesX(ax),  
        Size.Fixed(0.05),  
        Size.Fixed(0.2),  
    ])
    divider.set_vertical([Size.AxesY(ax)])

    Z, extent = get_demo_image()
    im = ax.imshow(Z, extent=extent)
    plt.colorbar(im, cax=ax_cb)
    ax_cb.yaxis.set_tick_params(labelright=False)

demo_locatable_axes_hard()
plt.show()
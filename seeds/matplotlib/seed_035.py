import matplotlib.pyplot as plt
from matplotlib import cbook


def get_demo_image():
    z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")  
    return z, (-3, 4, -4, 3)


def demo_locatable_axes_easy():
    from mpl_toolkits.axes_grid1 import make_axes_locatable

    fig, ax = plt.subplots()
    divider = make_axes_locatable(ax)

    ax_cb = divider.append_axes("right", size="5%", pad=0.05)
    fig.add_axes(ax_cb)

    Z, extent = get_demo_image()
    im = ax.imshow(Z, extent=extent)

    plt.colorbar(im, cax=ax_cb)
    ax_cb.yaxis.tick_right()
    ax_cb.yaxis.set_tick_params(labelright=False)

demo_locatable_axes_easy()
plt.show()

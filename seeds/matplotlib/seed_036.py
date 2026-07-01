import matplotlib.pyplot as plt
from matplotlib import cbook


def get_demo_image():
    z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")  
    return z, (-3, 4, -4, 3)


def demo_images_side_by_side():
    from mpl_toolkits.axes_grid1 import make_axes_locatable

    fig, ax = plt.subplots()
    divider = make_axes_locatable(ax)

    Z, extent = get_demo_image()
    ax2 = divider.append_axes("right", size="100%", pad=0.05)
    fig.add_axes(ax2)

    ax.imshow(Z, extent=extent)
    ax2.imshow(Z, extent=extent)
    ax2.yaxis.set_tick_params(labelleft=False)
    plt.show()

demo_images_side_by_side()
plt.show()
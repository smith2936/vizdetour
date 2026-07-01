import matplotlib.pyplot as plt
from matplotlib import cbook


def get_demo_image():
    z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")  
    return z, (-3, 4, -4, 3)


def demo_simple_image():
    fig, ax = plt.subplots()
    Z, extent = get_demo_image()
    im = ax.imshow(Z, extent=extent)
    cb = plt.colorbar(im)
    cb.ax.yaxis.set_tick_params(labelright=False)

demo_simple_image()
plt.show()
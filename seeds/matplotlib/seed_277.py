import matplotlib.pyplot as plt
import numpy as np

from matplotlib import cbook
from mpl_toolkits.axes_grid1.axes_rgb import RGBAxes


def get_rgb():
    Z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")
    Z[Z < 0] = 0.
    Z = Z / Z.max()

    R = Z[:13, :13]
    G = Z[2:, 2:]
    B = Z[:13, 2:]

    return R, G, B


def demo_rgb1():
    fig = plt.figure()
    ax = RGBAxes(fig, [0.1, 0.1, 0.8, 0.8], pad=0.0)
    r, g, b = get_rgb()
    ax.imshow_rgb(r, g, b)
    
demo_rgb1()
plt.show()
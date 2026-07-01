import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.axisartist import Axes
from mpl_toolkits.axisartist.grid_helper_curvelinear import GridHelperCurveLinear


def curvelinear_test1():
    fig = plt.figure(figsize=(7, 4))

    def tr(x, y): return x, y - x
    def inv_tr(x, y): return x, y + x

    grid_helper = GridHelperCurveLinear((tr, inv_tr))

    ax1 = fig.add_subplot(1, 2, 1, axes_class=Axes, grid_helper=grid_helper)

    xx, yy = tr(np.array([3, 6]), np.array([5, 10]))
    ax1.plot(xx, yy)

    ax1.set_aspect(1)
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 10)

    ax1.axis["t"] = ax1.new_floating_axis(0, 3)
    ax1.axis["t2"] = ax1.new_floating_axis(1, 7)
    ax1.grid(True, zorder=0)


curvelinear_test1()
plt.show()
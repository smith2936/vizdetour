import matplotlib.pyplot as plt

def draw_circle(ax):
    from matplotlib.patches import Circle
    from mpl_toolkits.axes_grid1.anchored_artists import AnchoredDrawingArea
    ada = AnchoredDrawingArea(20, 20, 0, 0,
                              loc='upper right', pad=0., frameon=False)
    p = Circle((10, 10), 10)
    ada.da.add_artist(p)
    ax.add_artist(ada)

fig, ax = plt.subplots()
ax.set_aspect(1.)

draw_circle(ax)

plt.show()
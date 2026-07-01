import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

fig, (ax, ax2) = plt.subplots(1, 2, figsize=[5.5, 2.8])

axins = inset_axes(ax, width=1.3, height=0.9)
axins2 = inset_axes(ax, width="30%", height="40%", loc="lower left")
axins3 = inset_axes(ax2, width="30%", height=1., loc="upper left")
axins4 = inset_axes(ax2, width="20%", height="20%", loc="lower right", borderpad=1)

for axi in [axins, axins2, axins3, axins4]:
    axi.tick_params(labelleft=False, labelbottom=False)

plt.show()
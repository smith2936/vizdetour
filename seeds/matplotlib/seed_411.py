import matplotlib.pyplot as plt
from mpl_toolkits.axisartist.parasite_axes import HostAxes

fig = plt.figure()
host = fig.add_axes((0.15, 0.1, 0.65, 0.8), axes_class=HostAxes)
par1 = host.get_aux_axes(viewlim_mode=None, sharex=host)

host.axis["right"].set_visible(False)

par1.axis["right"].set_visible(True)
par1.axis["right"].major_ticklabels.set_visible(True)
par1.axis["right"].label.set_visible(True)

p2, = par1.plot([0, 1, 2], [0, 3, 2], label="Temperature")
par1.set(ylim=(0, 4), ylabel="Temperature")

par1.axis["right"].label.set_color(p2.get_color())

plt.show()
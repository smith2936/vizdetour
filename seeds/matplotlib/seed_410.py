import matplotlib.pyplot as plt
from mpl_toolkits.axisartist.parasite_axes import HostAxes

fig = plt.figure()
host = fig.add_axes((0.15, 0.1, 0.65, 0.8), axes_class=HostAxes)
par1 = host.get_aux_axes(viewlim_mode=None, sharex=host)
par2 = host.get_aux_axes(viewlim_mode=None, sharex=host)

host.axis["right"].set_visible(False)

par1.axis["right"].set_visible(True)
par1.axis["right"].major_ticklabels.set_visible(True)
par1.axis["right"].label.set_visible(True)

par2.axis["right2"] = par2.new_fixed_axis(loc="right", offset=(60, 0))

p1, = host.plot([0, 1, 2], [0, 1, 2], label="Density")
host.set(xlim=(0, 2), ylim=(0, 2), xlabel="Distance", ylabel="Density")

host.axis["left"].label.set_color(p1.get_color())

plt.show()
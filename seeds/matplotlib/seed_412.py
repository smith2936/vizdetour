import matplotlib.pyplot as plt
from mpl_toolkits.axisartist.parasite_axes import HostAxes

fig = plt.figure()
host = fig.add_axes((0.15, 0.1, 0.65, 0.8), axes_class=HostAxes)
par2 = host.get_aux_axes(viewlim_mode=None, sharex=host)

host.axis["right"].set_visible(False)

par2.axis["right2"] = par2.new_fixed_axis(loc="right", offset=(60, 0))

p3, = par2.plot([0, 1, 2], [50, 30, 15], label="Velocity")
par2.set(ylim=(1, 65), ylabel="Velocity")

par2.axis["right2"].label.set_color(p3.get_color())

plt.show()
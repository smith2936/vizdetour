import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist

fig = plt.figure(figsize=(5, 2))
fig.subplots_adjust(wspace=0.4, bottom=0.3)

ax2 = fig.add_subplot(122, axes_class=axisartist.Axes)
ax2.set_yticks([0.2, 0.8])
ax2.set_xticks([0.2, 0.8])
ax2.set_xlabel("ax2 X-label")
ax2.set_ylabel("ax2 Y-label")

ax2.axis[:].major_ticks.set_tick_out(False)

plt.show()
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist

fig = plt.figure(figsize=(5, 2))
fig.subplots_adjust(wspace=0.4, bottom=0.3)

ax1 = fig.add_subplot(121, axes_class=axisartist.Axes)
ax1.set_yticks([0.2, 0.8])
ax1.set_xticks([0.2, 0.8])
ax1.set_xlabel("ax1 X-label")
ax1.set_ylabel("ax1 Y-label")

ax1.axis[:].invert_ticklabel_direction()

plt.show()
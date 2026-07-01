import matplotlib.pyplot as plt

fig = plt.figure(figsize=(11, 6))
fig.suptitle("Showcase for pan/zoom events on overlapping axes.")

ax = fig.add_axes((.05, .05, .9, .9))
ax.patch.set_color(".75")
ax_twin = ax.twinx()

plt.show()
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(11, 6))
fig.suptitle("Showcase for pan/zoom events on overlapping axes.")

ax11 = fig.add_subplot(223, sharex=fig.add_subplot(221), sharey=fig.add_subplot(221))
ax11.set_forward_navigation_events(True)
ax11.text(.5, .5,
          "Visible patch\n\n"
          "Override capture behavior:\n\n"
          "ax.set_forward_navigation_events(True)",
          ha="center", va="center", transform=ax11.transAxes)

plt.show()
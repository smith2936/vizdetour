import matplotlib.pyplot as plt

fig = plt.figure(figsize=(11, 6))
fig.suptitle("Showcase for pan/zoom events on overlapping axes.")

ax22 = fig.add_subplot(224, sharex=fig.add_subplot(222), sharey=fig.add_subplot(222))
ax22.patch.set_visible(False)
ax22.set_forward_navigation_events(False)
ax22.text(.5, .5,
          "Invisible patch\n\n"
          "Override capture behavior:\n\n"
          "ax.set_forward_navigation_events(False)",
          ha="center", va="center", transform=ax22.transAxes)

plt.show()
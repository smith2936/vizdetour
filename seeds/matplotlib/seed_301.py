import matplotlib.pyplot as plt

fig = plt.figure(figsize=(11, 6))
fig.suptitle("Showcase for pan/zoom events on overlapping axes.")

ax2 = fig.add_subplot(222)
ax2_twin = ax2.twinx()
ax2.patch.set_visible(False)
ax2.text(.5, .5,
         "Invisible patch\n\n"
         "Pan/zoom events are\n"
         "forwarded to axes below",
         ha="center", va="center", transform=ax2.transAxes)

plt.show()
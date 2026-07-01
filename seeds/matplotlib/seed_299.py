import matplotlib.pyplot as plt

fig = plt.figure(figsize=(11, 6))
fig.suptitle("Showcase for pan/zoom events on overlapping axes.")

ax1 = fig.add_subplot(221)
ax1_twin = ax1.twinx()
ax1.text(.5, .5,
         "Visible patch\n\n"
         "Pan/zoom events are NOT\n"
         "forwarded to axes below",
         ha="center", va="center", transform=ax1.transAxes)

plt.show()
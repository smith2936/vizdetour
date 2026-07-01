from matplotlib import pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.offsetbox import AnchoredOffsetbox, AuxTransformBox, TextArea, VPacker


fig, ax = plt.subplots()
ax.set_aspect(1)

size = 0.1
text = r"1$^{\prime}$"
sizebar = AuxTransformBox(ax.transData)
sizebar.add_artist(Line2D([0, size], [0, 0], color="black"))
text = TextArea(text)
packer = VPacker(
    children=[sizebar, text], align="center", sep=5)
ax.add_artist(AnchoredOffsetbox(
    child=packer, loc="lower center", frameon=False,
    pad=0.1, borderpad=0.5))

plt.show()
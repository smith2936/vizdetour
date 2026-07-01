from matplotlib import pyplot as plt
from matplotlib.patches import Ellipse
from matplotlib.offsetbox import AnchoredOffsetbox, AuxTransformBox


fig, ax = plt.subplots()
ax.set_aspect(1)

aux_tr_box = AuxTransformBox(ax.transData)
aux_tr_box.add_artist(Ellipse((0, 0), width=0.1, height=0.15))
box = AnchoredOffsetbox(child=aux_tr_box, loc="lower left", frameon=True)
ax.add_artist(box)

plt.show()
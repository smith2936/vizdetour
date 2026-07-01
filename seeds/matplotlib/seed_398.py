import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import matplotlib.transforms as mtransforms

def add_fancy_patch_around(ax, bb, **kwargs):
    kwargs = {
        'facecolor': (1, 0.8, 1, 0.5),
        'edgecolor': (1, 0.5, 1, 0.5),
        **kwargs
    }
    fancy = FancyBboxPatch(bb.p0, bb.width, bb.height, **kwargs)
    ax.add_patch(fancy)
    return fancy

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.5, 5))

bb = mtransforms.Bbox([[-0.5, -0.5], [0.5, 0.5]])
add_fancy_patch_around(ax1, bb, boxstyle="square,pad=0",
                       edgecolor="black", facecolor="none", zorder=10)
add_fancy_patch_around(ax2, bb, boxstyle="square,pad=0",
                       edgecolor="black", facecolor="none", zorder=10)
ax1.set(xlim=(-1.5, 1.5), ylim=(-1.5, 1.5), aspect=2)
ax2.set(xlim=(-1.5, 1.5), ylim=(-1.5, 1.5), aspect=2)

fancy = add_fancy_patch_around(
    ax1, bb, boxstyle="round,pad=0.5")
ax1.set_title("aspect=2\nmutation_aspect=1")

fancy = add_fancy_patch_around(
    ax2, bb, boxstyle="round,pad=0.5", mutation_aspect=0.5)
ax2.set_title("aspect=2\nmutation_aspect=0.5")

plt.show()
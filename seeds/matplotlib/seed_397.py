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

def draw_control_points_for_patches(ax):
    for patch in ax.patches:
        patch.axes.plot(*patch.get_path().vertices.T, ".",
                        c=patch.get_edgecolor())

fig, axs = plt.subplots(2, 2, figsize=(8, 8))

bb = mtransforms.Bbox([[0.3, 0.4], [0.7, 0.6]])

ax = axs[0, 0]
add_fancy_patch_around(ax, bb, boxstyle="round,pad=0.1")
ax.set(xlim=(0, 1), ylim=(0, 1), aspect=1,
       title='boxstyle="round,pad=0.1"')

ax = axs[0, 1]
fancy = add_fancy_patch_around(ax, bb, boxstyle="round,pad=0.1")
fancy.set_boxstyle("round,pad=0.1,rounding_size=0.2")
ax.set(xlim=(0, 1), ylim=(0, 1), aspect=1,
       title='boxstyle="round,pad=0.1,rounding_size=0.2"')

ax = axs[1, 0]
add_fancy_patch_around(ax, bb, boxstyle="round,pad=0.1", mutation_scale=2)
ax.set(xlim=(0, 1), ylim=(0, 1), aspect=1,
       title='boxstyle="round,pad=0.1"\n mutation_scale=2')

ax = axs[1, 1]
add_fancy_patch_around(ax, bb, boxstyle="round,pad=0.1", mutation_aspect=0.5)
ax.set(xlim=(0, 1), ylim=(0, 1),
       title='boxstyle="round,pad=0.1"\nmutation_aspect=0.5')

for ax in axs.flat:
    draw_control_points_for_patches(ax)
    add_fancy_patch_around(ax, bb, boxstyle="square,pad=0",
                           edgecolor="black", facecolor="none", zorder=10)

fig.tight_layout()
plt.show()
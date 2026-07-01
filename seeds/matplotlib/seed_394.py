import matplotlib.pyplot as plt
import numpy as np

from matplotlib.cbook import get_sample_data
from matplotlib.image import BboxImage
from matplotlib.offsetbox import AnchoredOffsetbox, AuxTransformBox
from matplotlib.patches import PathPatch
from matplotlib.text import TextPath
from matplotlib.transforms import IdentityTransform


class PathClippedImagePatch(PathPatch):
    def __init__(self, path, bbox_image, **kwargs):
        super().__init__(path, **kwargs)
        self.bbox_image = BboxImage(
            self.get_window_extent, norm=None, origin=None)
        self.bbox_image.set_data(bbox_image)

    def set_facecolor(self, color):
        super().set_facecolor("none")

    def draw(self, renderer=None):
        self.bbox_image.set_clip_path(self._path, self.get_transform())
        self.bbox_image.draw(renderer)
        super().draw(renderer)


fig, ax1 = plt.subplots()

arr = plt.imread(get_sample_data("grace_hopper.jpg"))

text_path = TextPath((0, 0), "!?", size=150)
p = PathClippedImagePatch(text_path, arr, ec="k")

offsetbox = AuxTransformBox(IdentityTransform())
offsetbox.add_artist(p)

ao = AnchoredOffsetbox(loc='upper left', child=offsetbox, frameon=True,
                       borderpad=0.2)
ax1.add_artist(ao)

for usetex, ypos, string in [
        (False, 0.25, r"textpath supports mathtext"),
        (True, 0.05, r"textpath supports \TeX"),
]:
    text_path = TextPath((0, 0), string, size=20, usetex=usetex)

    p1 = PathPatch(text_path, ec="w", lw=3, fc="w", alpha=0.9)
    p2 = PathPatch(text_path, ec="none", fc="k")

    offsetbox2 = AuxTransformBox(IdentityTransform())
    offsetbox2.add_artist(p1)
    offsetbox2.add_artist(p2)

    from matplotlib.offsetbox import AnnotationBbox
    ab = AnnotationBbox(offsetbox2, (0.95, ypos),
                        xycoords='axes fraction',
                        boxcoords="offset points",
                        box_alignment=(1., 0.),
                        frameon=False,
                        )
    ax1.add_artist(ab)

ax1.imshow([[0, 1, 2], [1, 2, 3]], cmap="gist_gray_r",
           interpolation="bilinear", aspect="auto")

plt.show()
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.image import BboxImage
from matplotlib.offsetbox import AuxTransformBox, AnnotationBbox
from matplotlib.patches import PathPatch, Shadow
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


fig, ax2 = plt.subplots()

arr = np.arange(256).reshape(1, 256)

for usetex, xpos, string in [
        (False, 0.25,
         r"$\left[\sum_{n=1}^\infty\frac{-e^{i\pi}}{2^n}\right]$!"),
        (True, 0.75,
         r"$\displaystyle\left[\sum_{n=1}^\infty"
         r"\frac{-e^{i\pi}}{2^n}\right]$!"),
]:
    text_path = TextPath((0, 0), string, size=40, usetex=usetex)
    text_patch = PathClippedImagePatch(text_path, arr, ec="none")
    shadow1 = Shadow(text_patch, 1, -1, fc="none", ec="0.6", lw=3)
    shadow2 = Shadow(text_patch, 1, -1, fc="0.3", ec="none")

    offsetbox = AuxTransformBox(IdentityTransform())
    offsetbox.add_artist(shadow1)
    offsetbox.add_artist(shadow2)
    offsetbox.add_artist(text_patch)

    ab = AnnotationBbox(offsetbox, (xpos, 0.5), box_alignment=(0.5, 0.5))

    ax2.add_artist(ab)

ax2.set_xlim(0, 1)
ax2.set_ylim(0, 1)

plt.show()
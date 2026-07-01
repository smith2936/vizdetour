import matplotlib.pyplot as plt

from matplotlib import cbook
from matplotlib.colors import LightSource


def compare(z, cmap, ve=1):
    fig, axs = plt.subplots(ncols=2, nrows=2)
    for ax in axs.flat:
        ax.set(xticks=[], yticks=[])

    ls = LightSource(azdeg=315, altdeg=45)

    axs[0, 0].imshow(z, cmap=cmap)
    axs[0, 0].set(xlabel='Colormapped Data')

    axs[0, 1].imshow(ls.hillshade(z, vert_exag=ve), cmap='gray')
    axs[0, 1].set(xlabel='Illumination Intensity')

    rgb = ls.shade(z, cmap=cmap, vert_exag=ve, blend_mode='hsv')
    axs[1, 0].imshow(rgb)
    axs[1, 0].set(xlabel='Blend Mode: "hsv" (default)')

    rgb = ls.shade(z, cmap=cmap, vert_exag=ve, blend_mode='overlay')
    axs[1, 1].imshow(rgb)
    axs[1, 1].set(xlabel='Blend Mode: "overlay"')

    return fig


dem = cbook.get_sample_data('jacksboro_fault_dem.npz')
elev = dem['elevation']

fig = compare(elev, plt.colormaps["gist_earth"], ve=0.05)
fig.suptitle('Overlay Blending Looks Best with Rough Surfaces', y=0.95)

plt.show()
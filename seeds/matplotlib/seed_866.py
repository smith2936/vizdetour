import matplotlib.pyplot as plt
import numpy as np

gradient = np.linspace(0, 1, 256)
gradient = np.vstack((gradient))

def plot_color_gradients(cmap_category, cmap_list):
    nrows = len(cmap_list)
    figh = 0.35 + 0.15 + (nrows + (nrows-1)*0.1)*0.22
    fig, axs = plt.subplots(nrows=nrows, figsize=(6.4, figh))
    fig.subplots_adjust(top=1-.35/figh, bottom=.15/figh, left=0.2, right=0.99)

    axs[0].set_title(f"{cmap_category} colormaps", fontsize=14)

    for ax, cmap_name in zip(axs, cmap_list):
        ax.imshow(gradient, aspect='auto', cmap=cmap_name)
        ax.text(-.01, .5, cmap_name, va='center', ha='right', fontsize=10,
                transform=ax.transAxes)

    for ax in axs:
        ax.set_axis_off()

plot_color_gradients("Original and reversed ", ['viridis', 'viridis_r'])
plt.show()
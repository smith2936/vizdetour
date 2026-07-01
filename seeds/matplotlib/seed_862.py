import matplotlib.pyplot as plt


def test_rotation_mode_default(fig):
    ha_list = ["left", "center", "right"]
    va_list = ["top", "center", "baseline", "bottom"]
    axs = fig.subplots(len(va_list), len(ha_list), sharex=True, sharey=True,
                       subplot_kw=dict(aspect=1),
                       gridspec_kw=dict(hspace=0, wspace=0))

    for ha, ax in zip(ha_list, axs[-1, :]):
        ax.set_xlabel(ha)
    for va, ax in zip(va_list, axs[:, 0]):
        ax.set_ylabel(va)
    axs[0, 1].set_title("rotation_mode='default'", size="large")

    texts = {}

    for i, va in enumerate(va_list):
        for j, ha in enumerate(ha_list):
            ax = axs[i, j]

            ax.set(xticks=[], yticks=[])
            ax.axvline(0.5, color="skyblue", zorder=0)
            ax.axhline(0.5, color="skyblue", zorder=0)
            ax.plot(0.5, 0.5, color="C0", marker="o", zorder=1)

            tx = ax.text(0.5, 0.5, "Tpg",
                         size="x-large", rotation=40,
                         horizontalalignment=ha, verticalalignment=va,
                         rotation_mode="default")
            texts[ax] = tx

    fig.canvas.draw()
    for ax, text in texts.items():
        bb = text.get_window_extent().transformed(ax.transData.inverted())
        rect = plt.Rectangle((bb.x0, bb.y0), bb.width, bb.height,
                             facecolor="C1", alpha=0.3, zorder=2)
        ax.add_patch(rect)
test_rotation_mode_default(plt.figure(figsize=(6, 6)))
plt.show()
import matplotlib.pyplot as plt


def test_rotation_mode_anchor(fig):
    ha_list = ["left", "center", "right"]
    va_list = ["top", "center", "baseline", "bottom"]
    axs = fig.subplots(len(va_list), len(ha_list), sharex=True, sharey=True,
                       subplot_kw=dict(aspect=1),
                       gridspec_kw=dict(hspace=0, wspace=0))

    for ha, ax in zip(ha_list, axs[-1, :]):
        ax.set_xlabel(ha)
    for va, ax in zip(va_list, axs[:, 0]):
        ax.set_ylabel(va)
    axs[0, 1].set_title("rotation_mode='anchor'", size="large")

    kw = {"bbox": dict(boxstyle="square,pad=0.", ec="none", fc="C1", alpha=0.3)}

    for i, va in enumerate(va_list):
        for j, ha in enumerate(ha_list):
            ax = axs[i, j]

            ax.set(xticks=[], yticks=[])
            ax.axvline(0.5, color="skyblue", zorder=0)
            ax.axhline(0.5, color="skyblue", zorder=0)
            ax.plot(0.5, 0.5, color="C0", marker="o", zorder=1)

            ax.text(0.5, 0.5, "Tpg",
                    size="x-large", rotation=40,
                    horizontalalignment=ha, verticalalignment=va,
                    rotation_mode="anchor", **kw)
test_rotation_mode_anchor(plt.figure(figsize=(6, 6)))
plt.show()
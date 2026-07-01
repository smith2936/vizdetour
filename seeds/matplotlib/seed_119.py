import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from io import BytesIO

def text_to_rgba(s, *, dpi, **kwargs):
    fig = Figure(facecolor="none")
    fig.text(0, 0, s, **kwargs)
    with BytesIO() as buf:
        fig.savefig(buf, dpi=dpi, format="png", bbox_inches="tight",
                    pad_inches=0)
        buf.seek(0)
        rgba = plt.imread(buf)
    return rgba

fig = plt.figure()
rgba2 = text_to_rgba(r"some other string", color="red", fontsize=20, dpi=200)
fig.figimage(rgba2, 100, 150)
fig.text(100, 350, r"some other string", color="red", fontsize=20)

plt.show()
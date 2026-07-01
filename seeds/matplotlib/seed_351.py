import time
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(6, 3), layout='constrained')

np.random.seed(19680801)

num_series = 1000
num_points = 100
SNR = 0.10  
x = np.linspace(0, 4 * np.pi, num_points)

Y = np.cumsum(np.random.randn(num_series, num_points), axis=-1)

num_signal = round(SNR * num_series)
phi = (np.pi / 8) * np.random.randn(num_signal, 1)  
Y[-num_signal:] = (
    np.sqrt(np.arange(num_points))  
    * (np.sin(x - phi)
       + 0.05 * np.random.randn(num_signal, num_points))  
)

tic = time.time()
num_fine = 800
x_fine = np.linspace(x.min(), x.max(), num_fine)
y_fine = np.concatenate([np.interp(x_fine, x, y_row) for y_row in Y])
x_fine = np.broadcast_to(x_fine, (num_series, num_fine)).ravel()

cmap = plt.colormaps["plasma"]
cmap = cmap.with_extremes(bad=cmap(0))
h, xedges, yedges = np.histogram2d(x_fine, y_fine, bins=[400, 100])
pcm = ax.pcolormesh(xedges, yedges, h.T, cmap=cmap,
                    vmax=1.5e2, rasterized=True)
fig.colorbar(pcm, ax=ax, label="# points", pad=0)
ax.set_title("2d histogram and linear color scale")
toc = time.time()
print(f"{toc-tic:.3f} sec. elapsed")
plt.show()
import time
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(6, 2.5), layout='constrained')

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
ax.plot(x, Y.T, color="C0", alpha=0.1)
toc = time.time()
ax.set_title("Line plot with alpha")
print(f"{toc-tic:.3f} sec. elapsed")
plt.show()
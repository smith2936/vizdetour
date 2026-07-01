import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)
x, y = np.random.randn(2, 100)

fig, ax1 = plt.subplots()
ax1.xcorr(x, y, usevlines=True, maxlags=50, normed=True, lw=2)
ax1.grid(True)
ax1.set_title('Cross-correlation (xcorr)')

plt.show()
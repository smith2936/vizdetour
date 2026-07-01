import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)
x = np.random.randn(100)

fig, ax2 = plt.subplots()
ax2.acorr(x, usevlines=True, normed=True, maxlags=50, lw=2)
ax2.grid(True)
ax2.set_title('Auto-correlation (acorr)')

plt.show()
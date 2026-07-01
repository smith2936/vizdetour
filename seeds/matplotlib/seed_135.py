import matplotlib.pyplot as plt
import numpy as np

y = np.arange(0.0, 2, 0.01)
x1 = np.sin(2 * np.pi * y)
x2 = 1.2 * np.sin(4 * np.pi * y)

fig, [ax, ax1] = plt.subplots(1, 2, sharey=True, figsize=(6, 6))
ax.plot(x1, y, x2, y, color='black')
ax.fill_betweenx(y, x1, x2, where=x2 >= x1, facecolor='green')
ax.fill_betweenx(y, x1, x2, where=x2 <= x1, facecolor='red')
ax.set_title('fill_betweenx where')

x2_masked = np.ma.masked_greater(x2, 1.0)
ax1.plot(x1, y, x2_masked, y, color='black')
ax1.fill_betweenx(y, x1, x2_masked, where=x2_masked >= x1, facecolor='green')
ax1.fill_betweenx(y, x1, x2_masked, where=x2_masked <= x1, facecolor='red')
ax1.set_title('regions with x2 > 1 are masked')

plt.show()
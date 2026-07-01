import matplotlib.pyplot as plt
import numpy as np

x = np.array([0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0])
y = np.exp(-x)
xerr = 0.1
yerr = 0.2
uplims = np.array([0, 1, 0, 0, 0, 1, 0, 0, 0, 1], dtype=bool)

fig, ax = plt.subplots(figsize=(7, 4))

ax.errorbar(x, y + 0.5, xerr=xerr, yerr=yerr, uplims=uplims, linestyle='dotted')

ax.set_xlim(0, 5.5)
ax.set_title('Errorbar plot with upper limits')
plt.show()
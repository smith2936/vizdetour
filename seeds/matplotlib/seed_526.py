import matplotlib.pyplot as plt
import numpy as np

x = np.array([0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0])
y = np.exp(-x)

xerr = 0.2
yerr = np.full_like(x, 0.2)
yerr[[3, 6]] = 0.3

xlolims = np.array([0, 0, 1, 0, 1, 0, 0, 0, 1, 0], dtype=bool)
xuplims = np.array([0, 1, 0, 0, 0, 1, 0, 0, 0, 1], dtype=bool)
lolims = np.zeros_like(x, dtype=bool)
uplims = np.zeros_like(x, dtype=bool)
lolims[[6]] = True  
uplims[[3]] = True  

fig, ax = plt.subplots(figsize=(7, 4))

ax.errorbar(x, y + 2.1, xerr=xerr, yerr=yerr,
            xlolims=xlolims, xuplims=xuplims,
            uplims=uplims, lolims=lolims,
            marker='o', markersize=8,
            linestyle='none')

ax.set_xlim(0, 5.5)
ax.set_title('Errorbar plot with upper and lower limits on both x and y')
plt.show()
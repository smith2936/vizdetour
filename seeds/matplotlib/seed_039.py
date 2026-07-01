import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0.1, 4, 0.5)
y = np.exp(-x)
error = 0.1 + 0.2 * x

fig, ax0 = plt.subplots()
ax0.errorbar(x, y, yerr=error, fmt='-o')
ax0.set_title('variable, symmetric error')
plt.show()
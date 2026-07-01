
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(layout='constrained')

x = np.arange(0.0, 4*np.pi, 0.2)
ax.plot(x, np.sin(x), label='Line 1')
ax.plot(x, np.exp(-x/2), marker='o', label='Line 2')

ax.legend()
plt.show()
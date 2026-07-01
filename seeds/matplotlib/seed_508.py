
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(layout='constrained')

x = np.arange(0.0, 4*np.pi, 0.2)
ax.plot(x, np.sin(x), color='tab:green', label='Line 3')
ax.plot(x, np.exp(-x/4), color='tab:red', marker='^', label='Line 4')

ax.legend()
plt.show()
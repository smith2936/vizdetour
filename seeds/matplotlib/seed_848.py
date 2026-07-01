import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0, 10, 0.01)

ax1 = plt.subplot(211)
ax1.plot(t, np.sin(2*np.pi*t))

plt.show()
import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0, 10, 0.01)

ax2 = plt.subplot(212)
ax2.plot(t, np.sin(4*np.pi*t))

plt.show()
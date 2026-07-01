import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.01, 5.0, 0.01)
s1 = np.sin(2 * np.pi * t)

plt.subplot(311)
plt.plot(t, s1)
plt.tick_params('x', labelsize=6)
plt.show()
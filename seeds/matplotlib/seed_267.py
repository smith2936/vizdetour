import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0, 2.0, 0.01)
s2 = np.sin(4*np.pi*t)

plt.figure(2)
plt.plot(t, s2)

plt.show()
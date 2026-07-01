import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.01, 5.0, 0.01)
s2 = np.exp(-t)

plt.subplot(312)
plt.plot(t, s2)
plt.tick_params('x', labelbottom=False)
plt.show()
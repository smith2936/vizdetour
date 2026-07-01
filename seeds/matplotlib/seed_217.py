import matplotlib.pyplot as plt
import numpy as np

t2 = np.arange(0.0, 5.0, 0.02)
plt.plot(t2, np.cos(2*np.pi*t2), color='tab:orange', linestyle='--')
plt.show()
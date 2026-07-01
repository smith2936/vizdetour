import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.01, 5.0, 0.01)
s3 = np.sin(4 * np.pi * t)

plt.subplot(313)
plt.plot(t, s3)
plt.xlim(0.01, 5.0)
plt.show()
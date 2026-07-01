import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 1.0, 0.01)
y1 = np.sin(2*np.pi*x)
lines = plt.plot(x, y1)
l1 = lines[0]

print('Line setters')
plt.setp(l1)
print('Line getters')
plt.getp(l1)
plt.show()
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(layout='constrained')
x = np.arange(0, 10)
np.random.seed(19680801)
y = np.random.randn(len(x))
ax.plot(x, y)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Random data')

secax = ax.secondary_xaxis(0, transform=ax.transData)
secax.set_xlabel('Axis at Y = 0')
plt.show()
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 100)
y = 2 * np.sin(x)

fig, ax1 = plt.subplots(layout='constrained')
ax1.plot(x, y)
ax1.set_title('bottom-left spines')

ax1.spines.right.set_visible(False)
ax1.spines.top.set_visible(False)

plt.show()
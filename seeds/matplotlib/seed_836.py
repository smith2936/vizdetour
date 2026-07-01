import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 100)
y = 2 * np.sin(x)

fig, ax0 = plt.subplots(layout='constrained')
ax0.plot(x, y)
ax0.set_title('normal spines')

plt.show()
import matplotlib.pyplot as plt
import numpy as np

an = np.linspace(0, 2 * np.pi, 100)
fig, ax = plt.subplots()

ax.plot(3 * np.cos(an), 3 * np.sin(an))
ax.axis('equal')
ax.set_title('equal, looks like circle', fontsize=10)

plt.show()
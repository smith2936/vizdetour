import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.01, 10.0, 0.01)
data2 = np.sin(2 * np.pi * t)

fig, ax2 = plt.subplots()

color = 'tab:blue'
ax2.set_xlabel('time (s)')
ax2.set_ylabel('sin', color=color)
ax2.plot(t, data2, color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()
plt.show()
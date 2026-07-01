import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.01, 10.0, 0.01)
data1 = np.exp(t)

fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('time (s)')
ax1.set_ylabel('exp', color=color)
ax1.plot(t, data1, color=color)
ax1.tick_params(axis='y', labelcolor=color)

fig.tight_layout()
plt.show()
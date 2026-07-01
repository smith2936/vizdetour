import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0.01, 4.0, 0.01)
y = np.exp(-x)

fig, ax2 = plt.subplots(figsize=(3.2, 4), layout="constrained")
fig.suptitle('Inverted axis with ...')

ax2.plot(x, y)
ax2.xaxis.set_inverted(True)  
ax2.set_title('autoscaling: set_inverted(True)')
ax2.set_xlabel('decreasing x ⟶')
ax2.grid(True)

plt.show()
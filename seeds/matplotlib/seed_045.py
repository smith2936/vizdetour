import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0.01, 4.0, 0.01)
y = np.exp(-x)

fig, ax1 = plt.subplots(figsize=(3.2, 4), layout="constrained")
fig.suptitle('Inverted axis with ...')

ax1.plot(x, y)
ax1.set_xlim(4, 0)   
ax1.set_title('fixed limits: set_xlim(4, 0)')
ax1.set_xlabel('decreasing x ⟶')
ax1.grid(True)

plt.show()
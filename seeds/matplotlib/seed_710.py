import matplotlib.pyplot as plt
import numpy as np
from matplotlib import patheffects

fig, ax = plt.subplots(figsize=(6, 6))
nx = 101
x = np.linspace(0.0, 1.0, nx)
y = 0.3*np.sin(x*8) + 0.4
ax.plot(x, y, label="Curve", path_effects=[patheffects.withTickedStroke()])

ax.legend()
plt.show()
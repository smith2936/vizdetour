import matplotlib.pyplot as plt
import numpy as np

N = 37
x, y = np.mgrid[:N, :N]
Z = (np.cos(x*0.2) + np.sin(y*0.3))

Zpos = np.ma.masked_less(Z, 0)

fig, ax1 = plt.subplots(figsize=(4, 3))
pos = ax1.imshow(Zpos, cmap='Blues', interpolation='none')
fig.colorbar(pos, ax=ax1)
plt.show()
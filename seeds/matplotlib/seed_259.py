import matplotlib.pyplot as plt
import numpy as np

N = 37
x, y = np.mgrid[:N, :N]
Z = (np.cos(x*0.2) + np.sin(y*0.3))

Zneg = np.ma.masked_greater(Z, 0)

fig, ax2 = plt.subplots(figsize=(4, 3))
neg = ax2.imshow(Zneg, cmap='Reds_r', interpolation='none')
fig.colorbar(neg, ax=ax2, location='right', anchor=(0, 0.3), shrink=0.7)
plt.show()
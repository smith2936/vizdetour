import matplotlib.pyplot as plt
import numpy as np

nrows = 3
ncols = 5
Z = np.arange(nrows * ncols).reshape(nrows, ncols)
x = np.arange(ncols)  
y = np.arange(nrows)

fig, ax = plt.subplots()
ax.pcolormesh(x, y, Z[:-1, :-1], shading='flat', vmin=Z.min(), vmax=Z.max())

X, Y = np.meshgrid(x, y)
ax.plot(X.flat, Y.flat, 'o', color='m')
ax.set_xlim(-0.7, 5.2)
ax.set_ylim(-0.7, 3.2)
ax.set_title("shading='flat': X, Y, C same shape")

plt.show()
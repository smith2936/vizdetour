import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
delta = 0.025
x = y = np.arange(-3.0, 3.0, delta)
X, Y = np.meshgrid(x, y)
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
Z = (Z1 - Z2) * 2

im = plt.imshow(Z, interpolation='bilinear', cmap="gray",
                origin='lower', extent=(-3, 3, -3, 3))

im.set_url('https://www.google.com/')
plt.show()
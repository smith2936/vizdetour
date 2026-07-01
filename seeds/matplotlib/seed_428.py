import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 5)
X, Y = np.meshgrid(x, x)
U, V = 12 * X, 12 * Y

fig1, axs1 = plt.subplots(nrows=2, ncols=2)

axs1[0, 0].barbs(X, Y, U, V)
plt.show()
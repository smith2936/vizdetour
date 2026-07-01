import matplotlib.pyplot as plt
import numpy as np

theta = np.arange(0, 8*np.pi, 0.1)
a = 1
b = .2

dt = np.pi
x = a*np.cos(theta + dt)*np.exp(b*theta)
y = a*np.sin(theta + dt)*np.exp(b*theta)

dt = dt + np.pi/4.0
x2 = a*np.cos(theta + dt)*np.exp(b*theta)
y2 = a*np.sin(theta + dt)*np.exp(b*theta)

xf = np.concatenate((x, x2[::-1]))
yf = np.concatenate((y, y2[::-1]))

plt.fill(xf, yf)
plt.show()
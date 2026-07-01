import matplotlib.pyplot as plt
import numpy as np

d = np.arange(100).reshape(10, 10)  
x, y = np.meshgrid(np.arange(11), np.arange(11))

theta = 0.25*np.pi
xx = x*np.cos(theta) - y*np.sin(theta)  
yy = x*np.sin(theta) + y*np.cos(theta)  

fig, ax1 = plt.subplots(layout="constrained")

ax1.set_aspect(1)
ax1.pcolormesh(xx, yy, d)
ax1.set_title("No Rasterization")

plt.show()
import matplotlib.pyplot as plt
import numpy as np

d = np.arange(100).reshape(10, 10)  
x, y = np.meshgrid(np.arange(11), np.arange(11))

theta = 0.25*np.pi
xx = x*np.cos(theta) - y*np.sin(theta)  
yy = x*np.sin(theta) + y*np.cos(theta)  

fig, ax3 = plt.subplots(layout="constrained")

ax3.set_aspect(1)
ax3.pcolormesh(xx, yy, d)
ax3.text(0.5, 0.5, "Text", alpha=0.2,
         va="center", ha="center", size=50, transform=ax3.transAxes)
ax3.set_title("No Rasterization")

plt.show()
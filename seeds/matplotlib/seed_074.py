import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)
Z = np.random.rand(6, 10)
x = np.arange(-0.5, 10, 1)  
y = np.arange(4.5, 11, 1)  

fig, ax = plt.subplots()
ax.pcolormesh(x, y, Z)
plt.show()
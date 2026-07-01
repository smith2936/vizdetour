import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)

x = np.random.rand(10)
y = np.random.rand(10)
z = np.sqrt(x**2 + y**2)

fig, ax = plt.subplots()
ax.scatter(x, y, s=80, c=z, marker=r"$\clubsuit$")
ax.set_title(r"marker=r'\$\clubsuit\$'")
plt.show()
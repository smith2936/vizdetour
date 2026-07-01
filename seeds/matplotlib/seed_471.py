import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['axes.autolimit_mode'] = 'round_numbers'

np.random.seed(19680801)
dots = np.linspace(0.3, 1.2, 10)
X, Y = np.meshgrid(dots, dots)
x, y = X.ravel(), Y.ravel()

fig, ax = plt.subplots()
ax.scatter(x, y, c=x+y)
plt.show()
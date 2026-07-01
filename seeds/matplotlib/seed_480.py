import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 5)
y1 = np.arange(1, 5)
y2 = np.ones(y1.shape) * 4

fig, ax = plt.subplots()
ax.bar(x, y1, edgecolor='black', hatch=['--', '+', 'x', '\\'])
ax.bar(x, y2, bottom=y1, edgecolor='black',
       hatch=['*', 'o', 'O', '.'])

plt.show()
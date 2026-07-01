import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')

np.random.seed(19680801)

fig, ax1 = plt.subplots()
x, y = np.random.normal(size=(2, 200))
ax1.plot(x, y, 'o')

plt.show()
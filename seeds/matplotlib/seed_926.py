import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)  

dt = 0.001
t = np.arange(0.0, 10.0, dt)
r = np.exp(-t[:1000] / 0.05)  

fig = plt.figure()
left_inset_ax = fig.add_axes((.2, .6, .2, .2), facecolor='k')
left_inset_ax.plot(t[:len(r)], r)
left_inset_ax.set(title='Impulse response', xlim=(0, .2), xticks=[], yticks=[])

plt.show()
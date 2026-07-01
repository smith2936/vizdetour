import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)  

dt = 0.001
t = np.arange(0.0, 10.0, dt)
r = np.exp(-t[:1000] / 0.05)  
x = np.random.randn(len(t))
s = np.convolve(x, r)[:len(x)] * dt  

fig = plt.figure()
right_inset_ax = fig.add_axes((.65, .6, .2, .2), facecolor='k')
right_inset_ax.hist(s, 400, density=True)
right_inset_ax.set(title='Probability', xticks=[], yticks=[])

plt.show()
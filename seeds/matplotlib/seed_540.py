import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(layout='constrained')
x1_vals = np.arange(2, 11, 0.4)

x2_vals = x1_vals ** 2
ydata = 50.0 + 20 * np.random.randn(len(x1_vals))
ax.plot(x1_vals, ydata, label='Plotted data')
ax.plot(x1_vals, x2_vals, label=r'$x_2 = x_1^2$')
ax.set_xlabel(r'$x_1$')
ax.legend()


x1n = np.linspace(0, 20, 201)
x2n = x1n**2


def forward(x):
    return np.interp(x, x1n, x2n)


def inverse(x):
    return np.interp(x, x2n, x1n)


ax.axvline(np.sqrt(40), color="grey", ls="--")
ax.axvline(10, color="grey", ls="--")
secax = ax.secondary_xaxis('top', functions=(forward, inverse))
secax.set_xticks([10, 20, 40, 60, 80, 100])
secax.set_xlabel(r'$x_2$')

plt.show()
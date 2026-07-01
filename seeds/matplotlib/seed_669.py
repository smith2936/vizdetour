import matplotlib.pyplot as plt
import numpy as np

x = np.arange(400)
y = np.linspace(0.002, 1, 400)

def forward(x):
    return x**(1/2)

def inverse(x):
    return x**2

fig, ax = plt.subplots(figsize=(6, 4), layout='constrained')

ax.plot(x, y)
ax.set_yscale('function', functions=(forward, inverse))
ax.set_title('function: $x^{1/2}$')
ax.grid(True)
ax.set_yticks(np.arange(0, 1.2, 0.2))

plt.show()
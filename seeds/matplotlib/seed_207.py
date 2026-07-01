import matplotlib.pyplot as plt
import numpy as np

def format_axes(ax, title=None):
    ax.xaxis.get_minor_locator().set_params(subs=[2, 3, 4, 5, 6, 7, 8, 9])
    ax.grid()
    ax.xaxis.grid(which='minor')  
    linthresh = ax.xaxis.get_transform().linthresh
    linscale = ax.xaxis.get_transform().linscale
    ax.axvspan(-linthresh, linthresh, color='0.9')
    if title:
        ax.set_title(title.format(linthresh=linthresh, linscale=linscale))


x = np.linspace(-60, 60, 201)
y = np.linspace(0, 100.0, 201)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xscale('symlog', linscale=0.05)
format_axes(ax, title="Discontinuous gradient at linear/log transition")

plt.show()
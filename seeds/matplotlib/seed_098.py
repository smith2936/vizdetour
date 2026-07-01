import matplotlib.pyplot as plt

fig, ax = plt.subplots()

sc = ax.scatter([1, 2], [1, 2], c=[1, 2])
cbar = fig.colorbar(sc)
cbar.set_label("ZLabel", loc='top')

plt.show()
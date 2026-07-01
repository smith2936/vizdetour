import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import get_test_data

fig = plt.figure()

ax = fig.add_subplot(1, 1, 1, projection='3d')

X, Y, Z = get_test_data(0.05)
ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)

plt.show()
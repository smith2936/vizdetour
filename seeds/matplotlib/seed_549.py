import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

fig = plt.figure(figsize=(8, 6))
ax1 = fig.add_subplot(111, projection='3d')

X, Y, Z = axes3d.get_test_data(0.05)

ax1.plot_wireframe(X, Y, Z, rstride=10, cstride=0)
ax1.set_title("Column (x) stride set to 0")

plt.tight_layout()
plt.show()
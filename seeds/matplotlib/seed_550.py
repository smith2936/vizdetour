import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

fig = plt.figure(figsize=(8, 6))
ax2 = fig.add_subplot(111, projection='3d')

X, Y, Z = axes3d.get_test_data(0.05)

ax2.plot_wireframe(X, Y, Z, rstride=0, cstride=10)
ax2.set_title("Row (y) stride set to 0")

plt.tight_layout()
plt.show()
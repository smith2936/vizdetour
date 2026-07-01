import matplotlib.pyplot as plt
import numpy as np
import matplotlib.tri as mtri

fig = plt.figure(figsize=plt.figaspect(0.5))

u = np.linspace(0, 2.0 * np.pi, endpoint=True, num=50)
v = np.linspace(-0.5, 0.5, endpoint=True, num=10)
u, v = np.meshgrid(u, v)
u, v = u.flatten(), v.flatten()

x = (1 + 0.5 * v * np.cos(u / 2.0)) * np.cos(u)
y = (1 + 0.5 * v * np.cos(u / 2.0)) * np.sin(u)
z = 0.5 * v * np.sin(u / 2.0)

tri = mtri.Triangulation(u, v)

ax = fig.add_subplot(1, 2, 1, projection='3d')
ax.plot_trisurf(x, y, z, triangles=tri.triangles, cmap="Spectral")
ax.set_zlim(-1, 1)

plt.show()
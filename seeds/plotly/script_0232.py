import plotly.figure_factory as ff

import numpy as np
from scipy.spatial import Delaunay

u=np.linspace(-np.pi/2, np.pi/2, 60)
v=np.linspace(0, np.pi, 60)
u,v=np.meshgrid(u,v)
u=u.flatten()
v=v.flatten()

x = (np.sqrt(2)*(np.cos(v)*np.cos(v))*np.cos(2*u) + np.cos(u)*np.sin(2*v))/(2 - np.sqrt(2)*np.sin(3*u)*np.sin(2*v))
y = (np.sqrt(2)*(np.cos(v)*np.cos(v))*np.sin(2*u) - np.sin(u)*np.sin(2*v))/(2 - np.sqrt(2)*np.sin(3*u)*np.sin(2*v))
z = (3*(np.cos(v)*np.cos(v)))/(2 - np.sqrt(2)*np.sin(3*u)*np.sin(2*v))

points2D = np.vstack([u, v]).T
tri = Delaunay(points2D)
simplices = tri.simplices

fig = ff.create_trisurf(x=x, y=y, z=z,
                         colormap=['rgb(50, 0, 75)', 'rgb(200, 0, 200)', '#c8dcc8'],
                         show_colorbar=True,
                         simplices=simplices,
                         title=dict(text="Boy's Surface"))
fig.show(renderer="json")
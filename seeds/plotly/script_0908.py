import numpy as np
import plotly.graph_objects as go

# Define vector and scalar fields
x, y, z = np.mgrid[0:1:8j, 0:1:8j, 0:1:8j]
u =    np.sin(np.pi*x) * np.cos(np.pi*z)
v = -2*np.sin(np.pi*y) * np.cos(2*np.pi*z)
w = np.cos(np.pi*x)*np.sin(np.pi*z) + np.cos(np.pi*y)*np.sin(2*np.pi*z)
magnitude = np.sqrt(u**2 + v**2 + w**2)
mask1 = np.logical_and(y>=.4, y<=.6)
mask2 = y>.6

fig = go.Figure(go.Isosurface(
                      x=x.ravel(), y=y.ravel(), z=z.ravel(),
                      value=magnitude.ravel(),
                      isomin=1.9, isomax=1.9,
                      colorscale="BuGn",
                      name='isosurface'))


fig.add_trace(go.Cone(x=x[mask1], y=y[mask1], z=z[mask1],
                      u=u[mask1], v=v[mask1], w=w[mask1],
                      colorscale="Blues",
                      name='cones'
))
fig.add_trace(go.Streamtube(
                      x=x[mask2], y=y[mask2], z=z[mask2],
                      u=u[mask2], v=v[mask2], w=w[mask2],
                      colorscale="Reds",
                      name='streamtubes'
))
# Update all traces together
fig.update_traces(showlegend=True, showscale=False)
fig.update_layout(width=600, title_text='Exploration of a vector field using several traces')
fig.show(renderer="json")
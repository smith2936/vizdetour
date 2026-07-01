import plotly.graph_objects as go
import numpy as np

X, Y, Z = np.mgrid[-5:5:40j, -5:5:40j, -5:5:40j]

# ellipsoid
values = X * X * 0.5 + Y * Y + Z * Z * 2

fig = go.Figure(data=go.Isosurface(
    x=X.flatten(),
    y=Y.flatten(),
    z=Z.flatten(),
    value=values.flatten(),
    isomin=5,
    isomax=50,
    surface_fill=0.4,
    caps=dict(x_show=False, y_show=False),
    slices_z=dict(show=True, locations=[-1, -3,]),
    slices_y=dict(show=True, locations=[0]),
    ))
fig.show(renderer="json")
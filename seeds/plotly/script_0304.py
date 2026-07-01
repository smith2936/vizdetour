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
    opacity=0.6,
    isomin=10,
    isomax=50,
    surface_count=3,
    caps=dict(x_show=False, y_show=False)
    ))
fig.show(renderer="json")
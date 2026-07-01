import plotly.graph_objects as go
import numpy as np

X, Y, Z = np.mgrid[-5:5:40j, -5:5:40j, 0:5:20j]

values = X * X * 0.5 + Y * Y + Z * Z * 2

fig = go.Figure(data=go.Isosurface(
    x=X.flatten(),
    y=Y.flatten(),
    z=Z.flatten(),
    value=values.flatten(),
    isomin=30,
    isomax=50,
    surface=dict(count=3, fill=0.7, pattern='odd'),
    showscale=False, # remove colorbar
    caps=dict(x_show=True, y_show=True),
    ))

fig.update_layout(
    margin=dict(t=0, l=0, b=0), # tight layout
    scene_camera_eye=dict(x=1.86, y=0.61, z=0.98))
fig.show(renderer="json")
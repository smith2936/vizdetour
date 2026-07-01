import numpy as np
import plotly.graph_objects as go


X, Y, Z = np.mgrid[:1:20j, :1:20j, :1:20j]
vol = (X - 1)**2 + (Y - 1)**2 + Z**2


fig = go.Figure(data=go.Volume(
    x=X.flatten(), y=Y.flatten(), z=Z.flatten(),
    value=vol.flatten(),
    isomin=0.2,
    isomax=0.7,
    opacity=0.2,
    surface_count=21,
    caps= dict(x_show=True, y_show=True, z_show=True, x_fill=1), # with caps (default mode)
    ))

# Change camera view for a better view of the sides, XZ plane
# (see https://plotly.com/python/v3/3d-camera-controls/)
fig.update_layout(scene_camera = dict(
    up=dict(x=0, y=0, z=1),
    center=dict(x=0, y=0, z=0),
    eye=dict(x=0.1, y=2.5, z=0.1)
))

fig.show(renderer="json")
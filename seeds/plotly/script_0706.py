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
    slices_z=dict(show=True, locations=[0.4]),
    surface=dict(fill=0.5, pattern='odd'),
    caps= dict(x_show=False, y_show=False, z_show=False), # no caps
    ))

fig.show(renderer="json")
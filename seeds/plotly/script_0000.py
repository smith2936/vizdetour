import numpy as np
import itertools as it
import plotly.graph_objs as go

x, y = np.array([*zip(*it.combinations(range(20), 2))])
z = np.random.random(len(x))
fig = go.Figure()
fig.add_scatter3d(
    x=x, y=y, z=z,
    mode="markers",
    marker=dict(
        line=dict(width=0.1, color="black"), size=z*10, color=z,
        colorscale="Turbo", showscale=True,
    ),
)
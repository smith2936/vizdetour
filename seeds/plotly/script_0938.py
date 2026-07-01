import plotly.graph_objects as go
import numpy as np

l = 1000
N = 10000
steps = np.random.choice([-1, 1], size=(N, l)) + 0.05 * np.random.standard_normal((N, l)) # l steps
position = np.cumsum(steps, axis=1) # integrate all positions by summing steps values along time axis

fig = go.Figure(data=go.Histogram(x=position[:, -1])) # positions at final time step
fig.show(renderer="json")
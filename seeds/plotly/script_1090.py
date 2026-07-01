import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

N = 20
x = np.linspace(0, 1, N)

fig = make_subplots(1, 3)
for i in range(1, 4):
    fig.add_trace(go.Scatter(x=x, y=np.random.random(N)), 1, i)
fig.update_xaxes(matches='x')
fig.show(renderer="json")
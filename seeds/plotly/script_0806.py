import plotly.graph_objects as go
import numpy as np

x0 = np.random.randn(50)
x1 = np.random.randn(50) + 2 # shift mean

fig = go.Figure()
# Use x instead of y argument for horizontal plot
fig.add_trace(go.Box(x=x0))
fig.add_trace(go.Box(x=x1))

fig.show(renderer="json")
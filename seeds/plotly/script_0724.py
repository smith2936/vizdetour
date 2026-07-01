import plotly.graph_objects as go

import numpy as np

y = np.random.randn(500)
# Use `y` argument instead of `x` for horizontal histogram

fig = go.Figure(data=[go.Histogram(y=y)])
fig.show(renderer="json")
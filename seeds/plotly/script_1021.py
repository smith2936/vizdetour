import plotly.graph_objects as go

import numpy as np
np.random.seed(1)

x = np.random.uniform(-1, 1, size=500)
y = np.random.uniform(-1, 1, size=500)

fig = go.Figure(go.Histogram2dContour(
        x = x,
        y = y
))

fig.show(renderer="json")
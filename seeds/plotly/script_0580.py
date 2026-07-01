import plotly.figure_factory as ff
import plotly.graph_objects as go

import numpy as np

N = 50
x_start, x_end = -2.0, 2.0
y_start, y_end = -1.0, 1.0
x = np.linspace(x_start, x_end, N)
y = np.linspace(y_start, y_end, N)
X, Y = np.meshgrid(x, y)
source_strength = 5.0
x_source, y_source = -1.0, 0.0

# Compute the velocity field on the mesh grid
u = (source_strength/(2*np.pi) *
     (X - x_source)/((X - x_source)**2 + (Y - y_source)**2))
v = (source_strength/(2*np.pi) *
     (Y - y_source)/((X - x_source)**2 + (Y - y_source)**2))

# Create streamline figure
fig = ff.create_streamline(x, y, u, v,
                           name='streamline')

# Add source point
fig.add_trace(go.Scatter(x=[x_source], y=[y_source],
                          mode='markers',
                          marker_size=14,
                          name='source point'))

fig.show(renderer="json")
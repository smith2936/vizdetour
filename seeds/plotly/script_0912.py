import plotly.graph_objects as go
import numpy as np

x = np.linspace(1, 200, 30)
fig = go.Figure(go.Scatter(x=x, y=x**3))
fig.update_xaxes(type="log", range=[np.log10(0.8), np.log10(250)])
fig.update_yaxes(type="log")
fig.show(renderer="json")
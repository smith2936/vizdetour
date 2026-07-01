import plotly.graph_objects as go

fig = go.Figure(go.Scattersmith(imag=[0.5, 1, 2, 3], real=[0.5, 1, 2, 3]))
fig.show(renderer="json")
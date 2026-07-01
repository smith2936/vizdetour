import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[1, 2, 3, 4, 5],
    name="Positive"
))

fig.add_trace(go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[5, 4, 3, 2, 1],
    name="Negative"
))

fig.add_shape(
    showlegend=True,
    type="rect",
    x0=2,
    x1=4,
    y0=4.5,
    y1=5,
)

fig.show(renderer="json")
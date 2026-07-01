import plotly.graph_objects as go

fig = go.Figure()
fig.add_trace(go.Bar(name="first", x=["a", "b"], y=[1, 2]))
fig.add_trace(go.Bar(name="second", x=["a", "b"], y=[2, 1]))
fig.add_shape(
    name="first shape",
    showlegend=True,
    type="rect",
    xref="paper",
    line=dict(dash="dash"),
    x0=0.85,
    x1=0.95,
    y0=0,
    y1=1.5,
)
fig.add_trace(go.Bar(name="third", x=["a", "b"], y=[1, 2]))
fig.add_trace(go.Bar(name="fourth", x=["a", "b"], y=[2, 1]))

fig.show(renderer="json")
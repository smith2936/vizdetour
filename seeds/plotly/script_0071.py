import plotly.graph_objects as go

fig = go.Figure()
fig.add_trace(go.Bar(name="fourth", x=["a", "b"], y=[2,1], legendrank=5))
fig.add_trace(go.Bar(name="second", x=["a", "b"], y=[2,1], legendrank=4))
fig.add_trace(go.Bar(name="first", x=["a", "b"], y=[1,2], legendrank=2))
fig.add_trace(go.Bar(name="third", x=["a", "b"], y=[1,2], legendrank=3))
fig.add_shape(
    legendrank=1,
    showlegend=True,
    type="line",
    xref="paper",
    line=dict(dash="5px"),
    x0=0.05,
    x1=0.45,
    y0=1.5,
    y1=1.5,
)
fig.show(renderer="json")
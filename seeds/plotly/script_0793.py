import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=[0, 1, 2],
    y=[1, 1, 1],
    mode="lines+markers+text",
    name="Lines, Markers and Text",
    text=["Text A", "Text B", "Text C"],
    textposition="top right",
    textfont=dict(
        family="sans serif",
        size=18,
        color="crimson"
    )
))

fig.add_trace(go.Scatter(
    x=[0, 1, 2],
    y=[2, 2, 2],
    mode="lines+markers+text",
    name="Lines and Text",
    text=["Text G", "Text H", "Text I"],
    textposition="bottom center",
    textfont=dict(
        family="sans serif",
        size=18,
        color="LightSeaGreen"
    )
))

fig.update_layout(showlegend=False)

fig.show(renderer="json")
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[2, 1, 6, 4, 4],
    hovertext=["Text A", "Text B", "Text C", "Text D", "Text E"],
    hoverinfo="text",
    marker=dict(
        color="green"
    ),
    showlegend=False
))

fig.show(renderer="json")
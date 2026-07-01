import plotly.graph_objects as go

fig = go.Figure(go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[2, 4, 3, 5, 4],
    mode="markers",
    marker=dict(
        size=25,
        color="white",
        line=dict(width=2, color="blue", dash="dot")
    )
))

fig.show(renderer="json")
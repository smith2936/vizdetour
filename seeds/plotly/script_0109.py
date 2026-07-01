import plotly.graph_objects as go

fig = go.Figure(
    data=[go.Scatter(
        mode="markers+text",
        x=[10,20],
        y=[20, 10],
        text=["Point A", "Point B"]
    )],
    layout=dict(height=400, width=400, template="none")
)
fig.show(renderer="json")
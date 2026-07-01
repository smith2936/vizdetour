import plotly.graph_objects as go

fig = go.Figure(go.Bar(
    x = ["apples", "oranges", "pears"],
    y = [1, 2, 3]
))

fig.update_xaxes(
    showgrid=True,
    ticks="outside",
    tickson="boundaries",
    ticklen=20
)

fig.show(renderer="json")
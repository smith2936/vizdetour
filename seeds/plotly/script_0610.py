import plotly.graph_objects as go

values = [0, 11, 12, 13, 14, 15, 20, 30]
labels = ["container", "A1", "A2", "A3", "A4", "A5", "B1", "B2"]
parents = ["", "container", "A1", "A2", "A3", "A4", "container", "B1"]

fig = go.Figure(go.Treemap(
    labels = labels,
    values = values,
    parents = parents,
    root_color="lightblue"
))

fig.update_layout(
    treemapcolorway = ["pink", "lightgray"],
    margin = dict(t=50, l=25, r=25, b=25)
)
fig.show(renderer="json")
import plotly.graph_objects as go

labels = ["container", "A1", "A2", "A3", "A4", "A5", "B1", "B2"]
parents = ["", "container", "A1", "A2", "A3", "A4", "container", "B1"]

fig = go.Figure(go.Icicle(
    labels = labels,
    parents = parents,
    marker_colors = ["pink", "royalblue", "lightgray", "purple",
                     "cyan", "lightgray", "lightblue", "lightgreen"]))

fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
fig.show(renderer="json")
import plotly.graph_objects as go

styles = ["solid", "dot", "dash", "longdash", "dashdot", "longdashdot"]

fig = go.Figure(go.Scatter(
    x=list(range(len(styles))),
    y=[0] * len(styles),
    mode="markers+text",
    text=styles,
    textposition="bottom center",
    marker=dict(size=30, color="white", line=dict(color="blue", width=2, dash=styles))
))

fig.show(renderer="json")
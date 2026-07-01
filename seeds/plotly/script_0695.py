import plotly.graph_objects as go
from plotly.subplots import make_subplots

fig = make_subplots(rows=1, cols=2)

fig.add_trace(go.Scatter(x=[1, 2, 3], y=[1, 2, 3], mode="markers"), row=1, col=1)
fig.add_trace(go.Scatter(x=[1, 2, 3], y=[3, 2, 1], mode="markers"), row=1, col=2)

# Chevron shape spanning both subplots
# Path coordinates map to axis refs in order:
#   M 2.5 1.5  -> xref[0]=x,  yref[0]=y   (start in subplot 1)
#   L 1.5 2    -> xref[1]=x2, yref[1]=y2  (tip in subplot 2)
#   L 2.5 2.5  -> xref[2]=x,  yref[2]=y   (end in subplot 1)

fig.add_shape(
    type="path",
    path="M 2.5 1.5 L 1.5 2 L 2.5 2.5",
    xref=["x", "x2", "x"],
    yref=["y", "y2", "y"],
    line=dict(color="purple", width=3),
)

fig.show(renderer="json")
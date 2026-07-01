import plotly.graph_objects as go
from plotly.subplots import make_subplots

fig = make_subplots(rows=1, cols=2)

fig.add_trace(go.Scatter(x=[1, 2, 3], y=[4, 5, 6], mode="markers", marker=dict(size=10)), row=1, col=1)
fig.add_trace(go.Scatter(x=[1, 2, 3], y=[6, 5, 4], mode="markers", marker=dict(size=10)), row=1, col=2)

fig.add_shape(
  type="rect",
  xref=["x", "x2"],  # x0 uses the x-axis from subplot 1 ("x"), while x1 uses the x-axis from subplot 2 ("x2")
  yref=["y", "y2"],  # y0 uses the y-axis from subplot 1 ("y"), while y1 uses the y-axis from subplot 2 ("y2")
  x0=2, y0=4.5,
  x1=3, y1=5.5,
  fillcolor="rgba(255, 0, 0, 0.2)",
  line=dict(color="red", width=2),
)

fig.show(renderer="json")
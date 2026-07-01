import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Create Subplots
fig = make_subplots(rows=2, cols=2)

fig.add_trace(go.Scatter(x=[2, 6], y=[1,1]), row=1, col=1)
fig.add_trace(go.Bar(x=[1,2,3], y=[4,5,6]), row=1, col=2)
fig.add_trace(go.Scatter(x=[10,20], y=[40,50]), row=2, col=1)
fig.add_trace(go.Bar(x=[11,13,15], y=[8,11,20]), row=2, col=2)

# Add shapes
fig.update_layout(
    shapes=[
        dict(type="line", xref="x", yref="y",
            x0=3, y0=0.5, x1=5, y1=0.8, line_width=3),
        dict(type="rect", xref="x2", yref='y2',
             x0=4, y0=2, x1=5, y1=6),
        dict(type="rect", xref="x3", yref="y3",
             x0=10, y0=20, x1=15, y1=30),
        dict(type="circle", xref="x4", yref="y4",
             x0=5, y0=12, x1=10, y1=18)])
fig.show(renderer="json")
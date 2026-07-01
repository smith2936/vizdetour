import plotly.graph_objects as go

fig = go.Figure(data=go.Cone(
    x=[1, 2, 3],
    y=[1, 2, 3],
    z=[1, 2, 3],
    u=[1, 0, 0],
    v=[0, 3, 0],
    w=[0, 0, 2],
    sizemode="absolute",
    sizeref=2,
    anchor="tip"))

fig.update_layout(
      scene=dict(domain_x=[0, 1],
                 camera_eye=dict(x=-1.57, y=1.36, z=0.58)))

fig.show(renderer="json")
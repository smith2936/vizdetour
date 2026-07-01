import plotly.graph_objects as go

fig= go.Figure(data=go.Isosurface(
    x=[0,0,0,0,1,1,1,1],
    y=[1,0,1,0,1,0,1,0],
    z=[1,1,0,0,1,1,0,0],
    value=[1,2,3,4,5,6,7,8],
    isomin=2,
    isomax=6,
))

fig.show(renderer="json")
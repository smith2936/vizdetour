import plotly.express as px
fig = px.scatter_polar(r=range(0,90,10), theta=range(0,90,10),
                       range_theta=[0,90], start_angle=0, direction="counterclockwise")
fig.show(renderer="json")
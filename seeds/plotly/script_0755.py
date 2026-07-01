import math
import plotly.graph_objects as go
import pandas as pd

# Read data from a csv
z_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv')

fig = go.Figure(data=go.Surface(z=z_data, showscale=False))
fig.update_layout(
    title=dict(text='Mt Bruno Elevation'),
    width=400, height=400,
    margin=dict(t=30, r=0, l=20, b=10)
)

angle = math.pi / 4 # 45 degrees

name = 'vertical is along y+z'
camera = dict(
    up=dict(x=0, y=math.cos(angle), z=math.sin(angle)),
    eye=dict(x=2, y=0, z=0)
)

fig.update_layout(scene_camera=camera, scene_dragmode='orbit', title=name)
fig.show(renderer="json")
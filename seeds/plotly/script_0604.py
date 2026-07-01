import pandas as pd
quakes = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/earthquakes-23k.csv')

import plotly.graph_objects as go
fig = go.Figure(go.Densitymap(lat=quakes.Latitude, lon=quakes.Longitude, z=quakes.Magnitude,
                                 radius=10))
fig.update_layout(map_style="https://tiles.stadiamaps.com/styles/stamen_watercolor.json?api_key=YOUR-API-KEY", map_center_lon=180)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show(renderer="json")
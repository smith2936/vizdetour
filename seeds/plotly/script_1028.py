import plotly.graph_objects as go

import urllib.request as request
import json

# Load heatmap data
response = request.urlopen(
    "https://raw.githubusercontent.com/plotly/datasets/master/custom_heatmap_colorscale.json")
dataset = json.load(response)

# Create and show figure
fig = go.Figure()

fig.add_trace(go.Heatmap(
    z=dataset["z"],
    colorbar=dict(
        title=dict(
            text="Surface Heat",
            side="top",
        ),
        tickmode="array",
        tickvals=[2, 25, 50, 75, 100],
        labelalias={100: "Hot", 50: "Mild", 2: "Cold"},
        ticks="outside"
    )
))

fig.show(renderer="json")
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/Nuclear%20Waste%20Sites%20on%20American%20Campuses.csv')
site_lat = df.lat
site_lon = df.lon
locations_name = df.text

fig = go.Figure()

fig.add_trace(go.Scattermap(
        lat=site_lat,
        lon=site_lon,
        mode='markers',
        marker=go.scattermap.Marker(
            size=17,
            color='rgb(255, 0, 0)',
            opacity=0.7
        ),
        text=locations_name,
        hoverinfo='text'
    ))

fig.add_trace(go.Scattermap(
        lat=site_lat,
        lon=site_lon,
        mode='markers',
        marker=go.scattermap.Marker(
            size=8,
            color='rgb(242, 177, 172)',
            opacity=0.7
        ),
        hoverinfo='none'
    ))

fig.update_layout(
    title=dict(text='Nuclear Waste Sites on Campus'),
    autosize=True,
    hovermode='closest',
    showlegend=False,
    map=dict(
        bearing=0,
        center=dict(
            lat=38,
            lon=-94
        ),
        pitch=0,
        zoom=3,
        style='light'
    ),
)

fig.show(renderer="json")
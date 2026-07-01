import plotly.figure_factory as ff
import plotly.express as px

df = px.data.carshare()

fig = ff.create_hexbin_map(
    data_frame=df, lat="centroid_lat", lon="centroid_lon",
    nx_hexagon=10, opacity=0.9, labels={"color": "Point Count"},
)
fig.update_layout(margin=dict(b=0, t=0, l=0, r=0))
fig.show(renderer="json")
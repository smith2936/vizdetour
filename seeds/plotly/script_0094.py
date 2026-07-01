import plotly.figure_factory as ff
import plotly.express as px

df = px.data.carshare()

fig = ff.create_hexbin_map(
    data_frame=df, lat="centroid_lat", lon="centroid_lon",
    nx_hexagon=10, opacity=0.5, labels={"color": "Point Count"},
    min_count=1,
)
fig.show(renderer="json")
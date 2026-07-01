import plotly.figure_factory as ff
import plotly.express as px
import numpy as np

df = px.data.carshare()

fig = ff.create_hexbin_map(
    data_frame=df, lat="centroid_lat", lon="centroid_lon",
    nx_hexagon=10, opacity=0.9, labels={"color": "Average Peak Hour"},
    color="peak_hour", agg_func=np.mean, color_continuous_scale="Icefire", range_color=[0,23]
)
fig.show(renderer="json")
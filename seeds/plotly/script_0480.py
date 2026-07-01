import plotly.figure_factory as ff
import plotly.express as px
import numpy as np

df = px.data.carshare()

fig = ff.create_hexbin_map(
    data_frame=df, lat="centroid_lat", lon="centroid_lon",
    nx_hexagon=10, opacity=0.9, labels={"color": "Summed Car.Hours"},
    color="car_hours", agg_func=np.sum, color_continuous_scale="Magma"
)
fig.show(renderer="json")
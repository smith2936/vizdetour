import plotly.express as px
from skimage import data
img = data.astronaut()
# Increase contrast by clipping the data range between 50 and 200
fig = px.imshow(img, zmin=50, zmax=200)
# We customize the hovertemplate to show both the data and the color values
# See https://plotly.com/python/hover-text-and-formatting/#customize-tooltip-text-with-a-hovertemplate
#fig.update_traces(hovertemplate="x: %{x} <br> y: %{y} <br> z: %{z} <br> color: %{color}")
fig.show(renderer="json")
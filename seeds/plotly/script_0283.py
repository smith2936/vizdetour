import plotly.express as px
from skimage import data
img = data.astronaut()
fig = px.imshow(img, binary_format="jpeg", binary_compression_level=0)
fig.show(renderer="json")
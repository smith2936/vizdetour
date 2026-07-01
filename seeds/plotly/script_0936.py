import plotly.express as px
from skimage import data
img = data.astronaut()
# Stretch the contrast of the red channel only, resulting in a more red image
fig = px.imshow(img, zmin=[50, 0, 0], zmax=[200, 255, 255])
fig.show(renderer="json")
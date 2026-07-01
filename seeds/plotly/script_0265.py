import plotly.express as px
from skimage import io
data = io.imread("https://github.com/scikit-image/skimage-tutorials/raw/main/images/cells.tif")
data = data.reshape((15, 4, 256, 256))[5:]
fig = px.imshow(data, animation_frame=0, facet_col=1, binary_string=True)
fig.show(renderer="json")
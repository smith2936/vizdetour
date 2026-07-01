import plotly.express as px
from skimage import io
data = io.imread("https://github.com/scikit-image/skimage-tutorials/raw/main/images/cells.tif")
data = data.reshape((5, 3, 4, 256, 256))
fig = px.imshow(data, animation_frame=0, facet_row=1, facet_col=2, binary_string=True)
fig.show(renderer="json")
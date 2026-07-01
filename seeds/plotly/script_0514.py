import plotly.express as px
from skimage import io
data = io.imread("https://github.com/scikit-image/skimage-tutorials/raw/main/images/cells.tif")
data = data.reshape((6, 10, 256, 256))[:3, :2]
fig = px.imshow(data, facet_row=0, facet_col=1, binary_string=True,
                labels={'facet_row':'group', 'facet_col':'slice'})
fig.show(renderer="json")
import plotly.express as px
from skimage import data
import numpy as np
img = np.arange(100).reshape((10, 10))
fig = px.imshow(img, binary_string=True)
# You can check that only x and y are displayed in the hover
# You can use a hovertemplate to override the hover information
# See https://plotly.com/python/hover-text-and-formatting/#customize-tooltip-text-with-a-hovertemplate
fig.show(renderer="json")
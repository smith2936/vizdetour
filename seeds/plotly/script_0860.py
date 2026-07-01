import plotly.express as px
import numpy as np
img = np.arange(100).reshape((10, 10))
fig = px.imshow(img, binary_string=True)
fig.show(renderer="json")
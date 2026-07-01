import plotly.express as px
import numpy as np
img = np.arange(100).reshape((10, 10))
fig = px.imshow(img, color_continuous_scale='gray')
fig.show(renderer="json")
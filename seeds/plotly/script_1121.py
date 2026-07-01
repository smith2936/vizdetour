import plotly.express as px
import numpy as np
img = np.arange(15**2).reshape((15, 15))
fig = px.imshow(img)
fig.show(renderer="json")
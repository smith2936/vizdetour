import numpy as np
import plotly.express as px

ar = np.arange(100).reshape((10, 10))
fig = px.scatter(ar, x=2, y=6, size=1, color=5)
fig.show(renderer="json")
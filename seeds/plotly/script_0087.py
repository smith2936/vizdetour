import plotly.express as px
import numpy as np

x = np.linspace(1, 200, 30)
fig = px.scatter(x=x, y=x**3, log_x=True, log_y=True, range_x=[0.8, 250])
fig.show(renderer="json")
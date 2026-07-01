import plotly.express as px
import numpy as np
N = 10000
np.random.seed(0)
fig = px.density_contour(dict(effect_size=5 + np.random.randn(N),
                              waiting_time=np.random.poisson(size=N)),
                         x="effect_size", y="waiting_time")
fig.show(renderer="json")
import plotly.express as px
import numpy as np
np.random.seed(1)

z = np.random.randn(20, 20)

fig = px.imshow(z, text_auto=".2f", color_continuous_scale='Greys', aspect="auto")
fig.show(renderer="json")
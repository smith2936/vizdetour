import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
np.random.seed(0)
z1, z2, z3 = np.random.random((3, 7, 7))
customdata = np.dstack((z2, z3))
fig = make_subplots(1, 2, subplot_titles=['z1', 'z2'])
fig.add_trace(go.Heatmap(
    z=z1,
    customdata=np.dstack((z2, z3)),
    hovertemplate='<b>z1:%{z:.3f}</b><br>z2:%{customdata[0]:.3f} <br>z3: %{customdata[1]:.3f} ',
    coloraxis="coloraxis1", name=''),
    1, 1)
fig.add_trace(go.Heatmap(
    z=z2,
    customdata=np.dstack((z1, z3)),
    hovertemplate='z1:%{customdata[0]:.3f} <br><b>z2:%{z:.3f}</b><br>z3: %{customdata[1]:.3f} ',
    coloraxis="coloraxis1", name=''),
    1, 2)
fig.update_layout(title_text='Hover to see the value of z1, z2 and z3 together')
fig.show(renderer="json")
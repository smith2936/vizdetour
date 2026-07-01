import plotly.graph_objects as go
import numpy as np

# Define random surface
N = 50
fig = go.Figure()
fig.add_trace(go.Mesh3d(x=(60*np.random.randn(N)),
                   y=(25*np.random.randn(N)),
                   z=(40*np.random.randn(N)),
                   opacity=0.5,
                   color='yellow'
                  ))
fig.add_trace(go.Mesh3d(x=(70*np.random.randn(N)),
                   y=(55*np.random.randn(N)),
                   z=(30*np.random.randn(N)),
                   opacity=0.5,
                   color='pink'
                  ))

fig.update_layout(scene = dict(
                      xaxis=dict(
                          title=dict(
                              text='X AXIS TITLE'
                          )
                      ),
                      yaxis=dict(
                          title=dict(
                              text='Y AXIS TITLE'
                          )
                      ),
                      zaxis=dict(
                          title=dict(
                              text='Z AXIS TITLE'
                          )
                      ),
                    ),
                    width=700,
                    margin=dict(r=20, b=10, l=10, t=10))

fig.show(renderer="json")
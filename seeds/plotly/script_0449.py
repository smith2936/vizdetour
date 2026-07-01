import plotly.graph_objects as go

fig = go.Figure(data=[go.Box(y=[0, 1, 1, 2, 3, 5, 8, 13, 21],
            boxpoints='all', # can also be outliers, or suspectedoutliers, or False
            jitter=0.3, # add some jitter for a better separation between points
            pointpos=-1.8 # relative position of points wrt box
              )])

fig.show(renderer="json")
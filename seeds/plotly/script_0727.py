import plotly.graph_objects as go

import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/96c0bd/sunburst-coffee-flavors-complete.csv')

fig = go.Figure()

fig.add_trace(go.Icicle(
    ids=df.ids,
    labels=df.labels,
    parents=df.parents,
    root_color="lightgrey"
))

fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))

fig.show(renderer="json")
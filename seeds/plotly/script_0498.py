import plotly.express as px

fig = px.line(y=[1, 0])

fig.update_xaxes(zeroline=True, zerolinewidth=2, zerolinecolor='LightPink')
fig.update_yaxes(zeroline=True, zerolinewidth=2, zerolinecolor='LightPink')

fig.show(renderer="json")
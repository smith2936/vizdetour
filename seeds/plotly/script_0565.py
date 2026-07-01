import plotly.express as px

fig = px.line(y=[1, 0])

fig.update_xaxes(title_text='Time')
fig.update_yaxes(title_text='Value A')

fig.show(renderer="json")
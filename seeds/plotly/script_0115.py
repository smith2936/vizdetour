import plotly.express as px

x = ['Team A', 'Team B', 'Team C']
y = ['Game One', 'Game Two', 'Game Three']

z = [[.1, .3, .5],
     [1.0, .8, .6],
     [.6, .4, .2]]

z_text = [['Win', 'Lose', 'Win'],
          ['Lose', 'Lose', 'Win'],
          ['Win', 'Win', 'Lose']]

fig = px.imshow(z, x=x, y=y, color_continuous_scale='Viridis', aspect="auto")
fig.update_traces(text=z_text, texttemplate="%{text}")
fig.update_xaxes(side="top")
fig.show(renderer="json")
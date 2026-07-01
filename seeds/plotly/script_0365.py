import plotly.figure_factory as ff

text = [['Team', 'Rank'], ['A', 1], ['B', 2], ['C', 3], ['D', 4], ['E', 5], ['F', 6]]

colorscale = [[0, '#272D31'],[.5, '#ffffff'],[1, '#ffffff']]
font=['#FCFCFC', '#00EE00', '#008B00', '#004F00', '#660000', '#CD0000', '#FF3030']

fig = ff.create_table(text, colorscale=colorscale, font_colors=font)
fig.layout.width=250
fig.show(renderer="json")
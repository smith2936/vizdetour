import plotly.figure_factory as ff

data_matrix = [['User', 'Language', 'Chart Type', '# of Views'],
               ['<a href="https://plotly.com/~empet/folder/home">empet</a>',
                '<a href="https://plotly.com/python/">Python</a>',
                '<a href="https://plotly.com/~empet/8614/">Network Graph</a>',
                298],
               ['<a href="https://plotly.com/~Grondo/folder/home">Grondo</a>',
                '<a href="https://plotly.com/matlab/">Matlab</a>',
                '<a href="https://plotly.com/~Grondo/42/">Subplots</a>',
                356],
               ['<a href="https://plotly.com/~Dreamshot/folder/home">Dreamshot</a>',
                '<a href="https://help.plot.ly/tutorials/">Web App</a>',
                '<a href="https://plotly.com/~Dreamshot/6575/_2014-us-city-populations/">Bubble Map</a>',
                262],
               ['<a href="https://plotly.com/~FiveThirtyEight/folder/home">FiveThirtyEight</a>',
                '<a href="https://help.plot.ly/tutorials/">Web App</a>',
                '<a href="https://plotly.com/~FiveThirtyEight/30/">Scatter</a>',
                692],
               ['<a href="https://plotly.com/~cpsievert/folder/home">cpsievert</a>',
                '<a href="https://plotly.com/r/">R</a>',
                '<a href="https://plotly.com/~cpsievert/1130/">Surface</a>',
                302]]

fig = ff.create_table(data_matrix)
fig.show(renderer="json")
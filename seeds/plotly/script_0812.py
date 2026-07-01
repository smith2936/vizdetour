import plotly.figure_factory as ff

import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')
df_sample = df[400:410]

colorscale = [[0, '#4d004c'],[.5, '#f2e5ff'],[1, '#ffffff']]

fig =  ff.create_table(df_sample, colorscale=colorscale)

fig.show(renderer="json")
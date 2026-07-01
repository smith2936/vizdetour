import plotly.figure_factory as ff

import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')
df_sample = df[100:120]

fig =  ff.create_table(df_sample)
fig.show(renderer="json")
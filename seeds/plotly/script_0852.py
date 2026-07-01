import plotly.express as px
import pandas as pd

df = (pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/Dash_Bio/Genetic/gene_conservation.csv')
        .set_index('0')
        .loc[['consensus','conservation']]
        .T
        .astype({"conservation": float}))

fig = px.bar(df, labels={ 'index': 'base' }, hover_name='consensus', y='conservation')
fig.show(renderer="json")
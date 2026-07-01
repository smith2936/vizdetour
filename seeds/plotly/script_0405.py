import plotly.express as px
import pandas as pd

df = px.data.gapminder()
gdp = df['pop'] * df['gdpPercap']
fig = px.bar(df, x='year', y=gdp, color='continent', labels={'y':'gdp'},
             hover_data=['country'],
             title='Evolution of world GDP')
fig.show(renderer="json")
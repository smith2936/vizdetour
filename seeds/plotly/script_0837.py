import plotly.express as px
import numpy as np
import pandas as pd

df = px.data.gapminder()
gdp = np.log(df['pop'] * df['gdpPercap'])  # NumPy array
fig = px.bar(df, x='year', y=gdp, color='continent', labels={'y':'log gdp'},
             hover_data=['country'],
             title='Evolution of world GDP')
fig.show(renderer="json")
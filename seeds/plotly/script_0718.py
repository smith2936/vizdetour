import plotly.express as px
import numpy as np
df = px.data.gapminder()
fig = px.scatter_3d(df, x='year', y='continent', z='pop', size='gdpPercap', color='lifeExp',
                    hover_data=['country'])
fig.update_layout(scene_zaxis_type="log")
fig.show(renderer="json")
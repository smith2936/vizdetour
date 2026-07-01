import plotly.graph_objects as go
import plotly.data as data

df = data.gapminder()

df_europe = df[df['continent'] == 'Europe']

trace1 = go.Scatter(x=df_europe[df_europe['country'] == 'France']['year'],
                    y=df_europe[df_europe['country'] == 'France']['lifeExp'],
                    mode='lines+markers',
                    zorder=3,
                    name='France',
                    marker=dict(size=15))

trace2 = go.Scatter(x=df_europe[df_europe['country'] == 'Germany']['year'],
                    y=df_europe[df_europe['country'] == 'Germany']['lifeExp'],
                    mode='lines+markers',
                    zorder=1,
                    name='Germany',
                    marker=dict(size=15))

trace3 = go.Scatter(x=df_europe[df_europe['country'] == 'Spain']['year'],
                    y=df_europe[df_europe['country'] == 'Spain']['lifeExp'],
                    mode='lines+markers',
                    zorder=2,
                    name='Spain',
                    marker=dict(size=15))

layout = go.Layout(title=dict(text='Life Expectancy in Europe Over Time'))

fig = go.Figure(data=[trace1, trace2, trace3], layout=layout)

fig.show(renderer="json")
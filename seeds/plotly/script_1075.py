import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import math

data = px.data.gapminder()
df_2007 = data[data['year']==2007]
df_2007 = df_2007.sort_values(['continent', 'country'])

bubble_size = []

for index, row in df_2007.iterrows():
    bubble_size.append(math.sqrt(row['pop']))

df_2007['size'] = bubble_size
continent_names = ['Africa', 'Americas', 'Asia', 'Europe', 'Oceania']
continent_data = {continent:df_2007.query("continent == '%s'" %continent)
                              for continent in continent_names}

fig = go.Figure()

for continent_name, df in continent_data.items():
    fig.add_trace(
        go.Scatter(
            x=df['gdpPercap'],
            y=df['lifeExp'],
            marker_size=df['size'],
            text=df['continent'],
            name=continent_name,

            # The next three parameters specify the hover text
            # Text supports just one customized field per trace
            # and is implemented here with text=df['continent'],
            # Custom data supports multiple fields through numeric indices in the hover template
            # In we weren't using the text parameter in our example,
            # we could instead add continent as a third customdata field.
            customdata=df[['country','pop']],
            hovertemplate=
                "<b>%{customdata[0]}</b><br>" +
                "<b>%{text}</b><br><br>" +
                "GDP per Capita: %{x:$,.0f}<br>" +
                "Life Expectancy: %{y:.0f}<br>" +
                "Population: %{customdata[1]:,.0f}" +
                "<extra></extra>",
        ))


fig.update_traces(
    mode='markers',
    marker={'sizemode':'area',
            'sizeref':10})

fig.update_layout(
    xaxis={
        'title':'GDP per capita',
        'type':'log'},
    yaxis={'title':'Life Expectancy (years)'})

fig.show(renderer="json")
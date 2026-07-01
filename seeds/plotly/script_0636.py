import plotly.express as px

df = px.data.gapminder().query("continent == 'Africa'")

fig = px.line(df, x="year", y="lifeExp", facet_col="country", facet_col_wrap=7,
              facet_row_spacing=0.04, # default is 0.07 when facet_col_wrap is used
              facet_col_spacing=0.04, # default is 0.03
              height=600, width=800,
              title="Life Expectancy in Africa")
fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
fig.update_yaxes(showticklabels=True)
fig.show(renderer="json")
import plotly.express as px

df = px.data.tips()
fig = px.scatter(df, x="total_bill", y="tip", facet_col="smoker", color="sex", 
                 trendline="ols", trendline_scope="overall", trendline_color_override="black")
fig.show(renderer="json")
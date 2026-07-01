import plotly.express as px

df = px.data.tips()
fig = px.scatter(df, x="total_bill", y="tip", symbol="smoker", color="sex", trendline="ols", trendline_scope="overall")
fig.show(renderer="json")
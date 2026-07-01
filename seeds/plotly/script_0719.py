import plotly.express as px
df = px.data.tips()
df["size"] = df["size"].astype(str)
df["size"] = df["size"].astype(float)
fig = px.scatter(df, x="total_bill", y="tip", color="size",
                 title="Numeric 'size' values mean continuous color")

fig.show(renderer="json")
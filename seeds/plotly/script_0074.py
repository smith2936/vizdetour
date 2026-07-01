import plotly.express as px
df = px.data.tips()
fig = px.scatter(df, x="total_bill", y="tip", color="day",
             color_discrete_sequence=["red", "blue"],
             title="<b>Ambiguous!</b> Explicit color sequence cycling because it is too short"
            )

fig.show(renderer="json")
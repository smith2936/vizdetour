import plotly.express as px
wide_df = px.data.medals_wide()

fig = px.bar(wide_df, x="nation", y=["gold", "silver", "bronze"], title="Wide-Form Input, relabelled",
            labels={"value": "count", "variable": "medal"})
fig.show(renderer="json")
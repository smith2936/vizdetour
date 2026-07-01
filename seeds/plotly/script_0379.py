import plotly.express as px
wide_df = px.data.medals_wide()

fig = px.bar(wide_df, x="nation", y=["gold", "silver", "bronze"],
             title="Wide-Form Input, styled",
             labels={"value": "Medal Count", "variable": "Medal", "nation": "Olympic Nation"},
             color_discrete_map={"gold": "gold", "silver": "silver", "bronze": "#c96"},
             template="simple_white"
            )
fig.update_layout(font_family="Rockwell", showlegend=False)
fig.show(renderer="json")
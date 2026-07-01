import plotly.express as px
import numpy as np

df = px.data.gapminder().query("year == 2007")
fig = px.scatter(df, y="lifeExp", x="pop", color=np.log10(df["pop"]), hover_name="country", log_x=True)

fig.update_layout(coloraxis_colorbar=dict(
    title=dict(text="Population"),
    tickvals=[6,7,8,9],
    ticktext=["1M", "10M", "100M", "1B"],
))
fig.show(renderer="json")
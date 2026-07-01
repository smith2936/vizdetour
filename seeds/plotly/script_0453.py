import plotly.graph_objects as go
import plotly.express as px
df = px.data.gapminder().query("year == 2007")

fig = go.Figure()

fig.add_trace(go.Scatter(mode="markers", x=df["gdpPercap"], y=df["lifeExp"] ))

fig.update_xaxes(type="log")
fig.show(renderer="json")
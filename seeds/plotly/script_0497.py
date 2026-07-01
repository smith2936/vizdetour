import plotly.graph_objects as go
import plotly.express as px
df = px.data.gapminder().query("year == 2007")

fig = go.Figure()

fig.add_trace(go.Scatter(mode="markers", x=df["gdpPercap"], y=df["lifeExp"] ))

fig.update_xaxes(type="log", range=[0,5]) # log range: 10^0=1, 10^5=100000
fig.update_yaxes(range=[0,100]) # linear range
fig.show(renderer="json")
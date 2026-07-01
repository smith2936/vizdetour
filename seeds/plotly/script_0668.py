import plotly.express as px

fig = px.scatter(x=[1, 2, 3], y=[1, 2, 3], title="Try panning or zooming!")

fig.add_annotation(text="Absolutely-positioned annotation",
                  xref="paper", yref="paper",
                  x=0.3, y=0.3, showarrow=False)

fig.show(renderer="json")
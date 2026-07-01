import pandas as pd
import plotly.express as px

df = px.data.iris()

fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                 facet_col="species", title="Using update_xaxes() With A Plotly Express Figure")

fig.update_xaxes(showgrid=False)

fig.show(renderer="json")
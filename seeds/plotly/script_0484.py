import pandas as pd
import plotly.express as px

df = px.data.iris()

fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                 title="Conditionally Updating Traces In A Plotly Express Figure With for_each_trace()")

fig.for_each_trace(
    lambda trace: trace.update(marker_symbol="square") if trace.name == "setosa" else (),
)

fig.show(renderer="json")
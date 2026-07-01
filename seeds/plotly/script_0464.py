import plotly.express as px
df = px.data.iris()
fig = px.parallel_coordinates(df, color="species_id",
                             color_continuous_scale=[(0.00, "red"),   (0.33, "red"),
                                                     (0.33, "green"), (0.66, "green"),
                                                     (0.66, "blue"),  (1.00, "blue")])
fig.show(renderer="json")
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/cone_plot_data.csv"
)

fig = go.Figure(
    data=go.Cone(
        x=df["x"],
        y=df["y"],
        z=df["z"],
        u=df["u"],
        v=df["v"],
        w=df["w"],
        sizemode="raw",
        sizeref=0.1,
        colorscale="Portland",
        cmin=0,
        cmax=80,
        hoverinfo="u+v+w+text",
        text="-> wind <-",
    ),
    layout=dict(
        width=900, height=600, scene=dict(camera=dict(eye=dict(x=1.2, y=0, z=0.6)))
    ),
)


fig.show(renderer="json")
import plotly.graph_objects as go
import pandas as pd

df = pd.DataFrame(dict(
    date=["2020-01-10", "2020-02-10", "2020-03-10", "2020-04-10", "2020-05-10", "2020-06-10"],
    value=[1,2,3,1,2,3]
))

fig = go.Figure()
fig.add_trace(go.Scatter(
    name="Raw Data",
    mode="markers+lines", x=df["date"], y=df["value"],
    marker_symbol="star"
))
fig.add_trace(go.Scatter(
    name="Start-aligned",
    mode="markers+lines", x=df["date"], y=df["value"],
    xperiod="M1",
    xperiodalignment="start"
))
fig.add_trace(go.Scatter(
    name="Middle-aligned",
    mode="markers+lines", x=df["date"], y=df["value"],
    xperiod="M1",
    xperiodalignment="middle"
))
fig.add_trace(go.Scatter(
    name="End-aligned",
    mode="markers+lines", x=df["date"], y=df["value"],
    xperiod="M1",
    xperiodalignment="end"
))
fig.add_trace(go.Bar(
    name="Middle-aligned",
    x=df["date"], y=df["value"],
    xperiod="M1",
    xperiodalignment="middle"
))
fig.update_xaxes(showgrid=True, ticklabelmode="period")
fig.show(renderer="json")
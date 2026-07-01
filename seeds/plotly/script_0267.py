import plotly.graph_objects as go
from plotly.data import tips

df = tips()

summed_values = df.groupby(by="day", as_index=False).sum(numeric_only=True)
day_order_mapping = {"Thur": 0, "Fri": 1, "Sat": 2, "Sun": 3}
summed_values["order"] = summed_values["day"].apply(lambda day: day_order_mapping[day])
summed_values = summed_values.sort_values(by="order")

days_of_week = summed_values["day"].values
total_bills = summed_values["total_bill"].values
number_of_diners = summed_values["size"].values


fig = go.Figure(
    data=go.Bar(
        x=days_of_week,
        y=number_of_diners,
        name="Total number of diners",
        marker=dict(color="paleturquoise"),
    )
)

fig.add_trace(
    go.Scatter(
        x=days_of_week,
        y=total_bills,
        yaxis="y2",
        name="Total bill amount",
        marker=dict(color="crimson"),
    )
)

fig.update_layout(
    legend=dict(orientation="h"),
    yaxis=dict(
        title=dict(text="Total number of diners"),
        side="left",
        range=[0, 250],
    ),
    yaxis2=dict(
        title=dict(text="Total bill amount"),
        side="right",
        range=[0, 2000],
        overlaying="y",
        tickmode="sync",
    ),
)

fig.show(renderer="json")
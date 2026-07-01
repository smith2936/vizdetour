import plotly.graph_objects as go
import pandas as pd

apple_df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv"
)

# Convert 'Date' column to datetime format
apple_df['Date'] = pd.to_datetime(apple_df['Date'])

# Set 'Date' column as index
apple_df.set_index('Date', inplace=True)

# Filter for 2016
apple_df_2016 = apple_df.loc['2016']

# Create figure and add line
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=apple_df_2016.index,
    y=apple_df_2016["AAPL.High"],
    mode="lines"
))

# Set custom x-axis labels
fig.update_xaxes(
    ticktext=["End of Q1", "End of Q2", "End of Q3", "End of Q4"],
    tickvals=["2016-04-01", "2016-07-01", "2016-10-01", apple_df_2016.index.max()],
)

# Prefix y-axis tick labels with dollar sign
fig.update_yaxes(tickprefix="$")

# Set figure title
fig.update_layout(title_text="Apple Stock Price")

fig.show(renderer="json")
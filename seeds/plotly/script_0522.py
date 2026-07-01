import plotly.graph_objects as go
import pandas as pd


df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/refs/heads/master/gss_2002_5_pt_likert.csv')

df.rename(columns={'Unnamed: 0':"Category"}, inplace=True)

#achieve the diverging effect by putting a negative sign on the "disagree" answers 
for v in ["Disagree","Strongly Disagree"]:
    df[v]=df[v]*-1

fig = go.Figure()
# this color palette conveys meaning:  blues for positive, red and orange for negative
color_by_category={
    "Strongly Agree":'darkblue',
    "Agree":'lightblue',
    "Disagree":'orange',
    "Strongly Disagree":'red',
}


# We want the legend to be ordered in the same order that the categories appear, left to right --
# which is different from the order in which we have to add the traces to the figure.
# since we need to create the "somewhat" traces before the "strongly" traces to display
# the segments in the desired order
legend_rank_by_category={
    "Strongly Disagree":1,
    "Disagree":2,
    "Agree":3,
    "Strongly Agree":4,
}
# Add bars for each category
for col in ["Disagree","Strongly Disagree","Agree","Strongly Agree"]:
    fig.add_trace(go.Bar(
        y=df["Category"], 
        x=df[col], 
        name=col, 
        orientation='h',
        marker=dict(color=color_by_category[col]),
        legendrank=legend_rank_by_category[col]
    ))

fig.update_layout(
   title="Reactions to statements from the 2002 General Social Survey:",
    yaxis_title = "",
    barmode='relative',  # Allows bars to diverge from the center
    plot_bgcolor="white",
)

fig.update_xaxes(
        title="Percent of Responses",
        zeroline=True,  # Ensure there's a zero line for divergence
        zerolinecolor="black",
        # use array tick mode to show that the counts to the left of zero are still positive.
        # this is hard coded; generalize this if you plan to create a function that takes unknown or widely varying data
        tickmode = 'array',     
        tickvals = [-50, 0, 50, 100],
        ticktext = [50, 0, 50, 100]
)

fig.show(renderer="json")
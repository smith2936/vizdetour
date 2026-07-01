import pandas as pd
import plotly.express as px

data = {
    "Quarter": ["Q1", "Q2", "Q3", "Q4"] * 3,
    "Region": ["North", "North", "North", "North", "South", "South", "South", "South", "West", "West", "West", "West"],
    "Outcome": [150, 200, 250, 300, 120, 180, 240, 310, 100, 150, 220, 280]
}
df = pd.DataFrame(data)


fig = px.bar(
    df, 
    x="Outcome", 
    y="Region",
    orientation="h",  
    facet_col="Quarter", 
    title="Number of Patients Served by Region and Quarter", 
    labels={"Outcome": "Patients Served", "Region": "Region"} 
)

## the section below is optional clean up to make this presentation ready

fig.update_layout(
    height=400,  #the Plotly default makes the bars awkwardly large; setting a height improves the display
    showlegend=False,  # the legend does not add anything
)

# remove the default "facet_variable =" text from the title of each facet graph
fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))  

# Remove duplicate axis labels
fig.for_each_yaxis(lambda axis: axis.update(title=None))
fig.for_each_xaxis(lambda axis: axis.update(title=None))
# add the one valuable axis label back in
fig.update_xaxes(title="Count", row=1, col=1)

fig.show(renderer="json")
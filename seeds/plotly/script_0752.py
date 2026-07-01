import plotly.express as px
fig = px.funnel_area(names=["The 1st","The 2nd", "The 3rd", "The 4th", "The 5th"],
                    values=[5, 4, 3, 2, 1])
fig.show(renderer="json")
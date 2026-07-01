import plotly.express as px
df = px.data.tips()
fig = px.bar(df, x="day", y="total_bill", color="smoker", barmode="group", facet_col="sex",
             category_orders={"day": ["Thur", "Fri", "Sat", "Sun"],
                              "smoker": ["Yes", "No"],
                              "sex": ["Male", "Female"]})
fig.show(renderer="json")
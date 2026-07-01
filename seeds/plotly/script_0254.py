import plotly.express as px
df = px.data.gapminder().query("year == 2007")
fig = px.bar(df, y="continent", x="pop", color="continent", orientation="h", hover_name="country",
             color_discrete_map={
                "Europe": "red",
                "Asia": "green",
                "Americas": "blue",
                "Oceania": "goldenrod",
                "Africa": "magenta"},
             category_orders={"continent": ["Oceania", "Europe", "Asia", "Africa", "Americas"]},
             title="Explicit color mapping with explicit ordering"
            )

fig.show(renderer="json")
import plotly.express as px

df = px.data.election()
df = df.melt(id_vars="district", value_vars=["Coderre", "Bergeron", "Joly"],
            var_name="candidate", value_name="votes")
geojson = px.data.election_geojson()

fig = px.choropleth(df, geojson=geojson, color="votes", facet_col="candidate",
                    locations="district", featureidkey="properties.district",
                    projection="mercator"
                   )
fig.update_geos(fitbounds="locations", visible=False)
fig.show(renderer="json")
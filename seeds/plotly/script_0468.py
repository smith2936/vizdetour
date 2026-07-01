import plotly.express as px
df = px.data.iris()

fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                 size='petal_length', hover_data=['petal_width'])


fig.update_layout(
        title=dict(text="Note: this is the Plotly title element.",
                 # keeping this title string short avoids getting the text cut off in small windows
                 # if you need longer text, consider 1) embedding your graphic on a web page and
                 # putting the note in the HTML to use the browser's automated word wrap,
                 # 2) using this approach and also specifying a graph width that shows the whole title,
                 # or 3) using <BR> tags to wrap the text onto multiple lines
                yref="container",
                y=0.005,
                 # The "paper" x-coordinates lets us align this with either the right or left
                 # edge of the plot region.
                 # The code to align this flush with the right edge of the plot area is
                 # predictable and simple.
                 # Putting the title in the lower left corner, aligned with the left edge of the axis labeling would
                 # require graph specific coordinate adjustments.
                xref="paper",
                xanchor="right",
                x=1,
                font=dict(size=12)),
                plot_bgcolor="white",

  # We move the legend out of the right margin so the right-aligned note is
  # flush with the right most element of the graph.
  # Here we put the legend in a corner of the graph region
  # because it has consistent coordinates at all screen resolutions.
  legend=dict(
                yanchor="top",
                y=1,
                xanchor="right",
                x=1,
                borderwidth=1)
                )

# Insert a title by repurposing an annotation
fig.add_annotation(
    yref="paper",
    yanchor="bottom",
    y=1.025,  # y = 1 is the top of the plot area; the top is typically uncluttered, so placing
              # the bottom of the title slightly above the graph region works on a wide variety of graphs
            text="This title is a Plotly annotation",

    # Center the title horizontally over the plot area
    xref="paper",
    xanchor="center",
    x=0.5,

    showarrow=False,
    font=dict(size=18)
    )

fig.show(renderer="json")
import plotly.express as px

df = px.data.stocks(indexed=True)
fig = px.line(df)
fig.add_hline(y=1, line_dash="dot",
              annotation_text="Jan 1, 2018 baseline",
              annotation_position="bottom right",
              annotation_font_size=20,
              annotation_font_color="blue"
             )
fig.add_vrect(x0="2018-09-24", x1="2018-12-18",
              annotation_text="decline", annotation_position="top left",
              annotation=dict(font_size=20, font_family="Times New Roman"),
              fillcolor="green", opacity=0.25, line_width=0)
fig.show(renderer="json")
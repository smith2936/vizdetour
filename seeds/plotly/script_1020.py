import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scattergeo(
    lat=[45.5, 43.4, 49.13, 51.1, 53.34, 45.24, 44.64, 48.25, 49.89, 50.45],
    lon=[-73.57, -79.24, -123.06, -114.1, -113.28, -75.43, -63.57, -123.21, -97.13,
         -104.6],
    marker={
        "color": ["MidnightBlue", "IndianRed", "MediumPurple", "Orange", "Crimson",
                  "LightSeaGreen", "RoyalBlue", "LightSalmon", "DarkOrange", "MediumSlateBlue"],
        "line": {
            "width": 1
        },
        "size": 10
    },
    mode="markers+text",
    name="",
    text=["Montreal", "Toronto", "Vancouver", "Calgary", "Edmonton", "Ottawa",
          "Halifax",
          "Victoria", "Winnipeg", "Regina"],
    textfont={
        "color": ["MidnightBlue", "IndianRed", "MediumPurple", "Gold", "Crimson",
                  "LightSeaGreen",
                  "RoyalBlue", "LightSalmon", "DarkOrange", "MediumSlateBlue"],
        "family": ["Arial, sans-serif", "Balto, sans-serif", "Courier New, monospace",
                   "Droid Sans, sans-serif", "Droid Serif, serif",
                   "Droid Sans Mono, sans-serif",
                   "Gravitas One, cursive", "Old Standard TT, serif",
                   "Open Sans, sans-serif",
                   "PT Sans Narrow, sans-serif", "Raleway, sans-serif",
                   "Times New Roman, Times, serif"],
        "size": [22, 21, 20, 19, 18, 17, 16, 15, 14, 13]
    },
    textposition=["top center", "middle left", "top center", "bottom center",
                  "top right",
                  "middle left", "bottom right", "bottom left", "top right",
                  "top right"]
))

fig.update_layout(
    title_text="Canadian cities",
    geo=dict(
        lataxis=dict(range=[40, 70]),
        lonaxis=dict(range=[-130, -55]),
        scope="north america"
    )
)

fig.show(renderer="json")
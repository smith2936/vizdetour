import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/globe_contours.csv')
df.head()


scl = ['rgb(213,62,79)', 'rgb(244,109,67)', 'rgb(253,174,97)', \
    'rgb(254,224,139)', 'rgb(255,255,191)', 'rgb(230,245,152)', \
    'rgb(171,221,164)', 'rgb(102,194,165)', 'rgb(50,136,189)'
]
n_colors = len(scl)

fig = go.Figure()

for i, (lat, lon) in enumerate(zip(df.columns[::2], df.columns[1::2])):
    fig.add_trace(go.Scattergeo(
        lon = df[lon],
        lat = df[lat],
        mode = 'lines',
        line = dict(width = 2, color = scl[i % n_colors]
        )))

fig.update_layout(
    title_text = 'Contour lines over globe<br>(Click and drag to rotate)',
    showlegend = False,
    geo = dict(
        showland = True,
        showcountries = True,
        showocean = True,
        countrywidth = 0.5,
        landcolor = 'rgb(230, 145, 56)',
        lakecolor = 'rgb(0, 255, 255)',
        oceancolor = 'rgb(0, 255, 255)',
        projection = dict(
            type = 'orthographic',
            rotation = dict(
                lon = -100,
                lat = 40,
                roll = 0
            )
        ),
        lonaxis = dict(
            showgrid = True,
            gridcolor = 'rgb(102, 102, 102)',
            gridwidth = 0.5
        ),
        lataxis = dict(
            showgrid = True,
            gridcolor = 'rgb(102, 102, 102)',
            gridwidth = 0.5
        )
    )
)

fig.show(renderer="json")
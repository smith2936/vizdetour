import plotly.graph_objects as go

import numpy as np
np.random.seed(1)
from scipy.signal import savgol_filter

# Simulate spectroscopy data
def simulated_absorption(mu, sigma, intensity):
    data = [np.random.normal(mu[i], sigma[i], intensity[i]) for i in range(len(mu))]
    hists = [np.histogram(d, 1000, range=(200, 500), density=True) for d in data]
    ys = [y for y, x in hists]
    s = savgol_filter(np.max(ys, axis=0), 41, 3)
    return hists[0][1], s

mus = [[290, 240, 260], [330, 350]]
sigmas = [[4, 6, 10], [5, 4]]
intensities = [[100000, 300000, 700000], [40000, 20000]]
simulated_absorptions = [simulated_absorption(m, s, i) for m, s, i in
                         zip(mus, sigmas, intensities)]

# Create figure
fig = go.Figure()

# Create traces from data
names = ["Benzene", "Naphthalene"]
for (x, y), n in zip(simulated_absorptions, names):
    fig.add_trace(go.Scatter(x=x, y=y, name=n))

# Add images
fig.add_layout_image(
    dict(
        source="https://raw.githubusercontent.com/michaelbabyn/plot_data/master/benzene.png",
        x=0.75,
        y=0.65,
    ))
fig.add_layout_image(dict(
        source="https://raw.githubusercontent.com/michaelbabyn/plot_data/master/naphthalene.png",
        x=0.9,
        y=0.3,
        )
)
fig.update_layout_images(dict(
        xref="paper",
        yref="paper",
        sizex=0.3,
        sizey=0.3,
        xanchor="right",
        yanchor="bottom"
))

# Add annotations
fig.update_layout(
    annotations=[
        dict(
            x=93.0 / 300,
            y=0.07 / 0.1,
            xref="paper",
            yref="paper",
            showarrow=True,
            arrowhead=0,
            opacity=0.5,
            ax=250,
            ay=-40,
        ),
        dict(
            x=156.0 / 300,
            y=0.04 / 0.1,
            xref="paper",
            yref="paper",
            showarrow=True,
            arrowhead=0,
            opacity=0.5,
            ax=140,
            ay=-10,
        )
    ]
)

# Configure axes
fig.update_xaxes(title_text="Wavelength")
fig.update_yaxes(title_text="Absorption", hoverformat=".3f")

# Configure other layout properties
fig.update_layout(
    title_text="Absorption Frequencies of Benzene and Naphthalene",
    height=500,
    width=900,
    template="plotly_white"
)

fig.show(renderer="json")
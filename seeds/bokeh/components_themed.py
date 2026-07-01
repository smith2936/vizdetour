from bokeh.io import curdoc
from bokeh.plotting import figure, show
from bokeh.sampledata.penguins import data
from bokeh.transform import factor_cmap, factor_mark

SPECIES = ['Adelie', 'Chinstrap', 'Gentoo']
MARKERS = ['hex', 'circle_x', 'triangle']

p = figure(title = "Penguin size")
p.xaxis.axis_label = "Flipper Length (mm)"
p.yaxis.axis_label = "Body Mass (g)"

p.scatter("flipper_length_mm", "body_mass_g", source=data, legend_group="species", fill_alpha=0.4, size=12,
          marker=factor_mark('species', MARKERS, SPECIES),
          color=factor_cmap('species', 'Category10_3', SPECIES))

p.legend.background_fill_color = "#3f3f3f"

curdoc().add_root(p)
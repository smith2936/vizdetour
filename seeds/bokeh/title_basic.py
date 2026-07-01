from bokeh.io import curdoc
from bokeh.plotting import figure, show

p = figure(title="Basic Title", width=300, height=300)

p.scatter([1, 2], [3, 4])

curdoc().add_root(p)
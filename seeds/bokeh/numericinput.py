from bokeh.io import curdoc
from bokeh.io import show
from bokeh.models import NumericInput

numeric_input = NumericInput(value=1, low=1, high=10, title="Enter a number between 1 and 10:")

curdoc().add_root(numeric_input)
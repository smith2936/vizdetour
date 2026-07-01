from bokeh.io import curdoc
from bokeh.io import show
from bokeh.models import FileInput

file_input = FileInput()

curdoc().add_root(file_input)
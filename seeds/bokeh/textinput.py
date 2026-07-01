from bokeh.io import curdoc
from bokeh.io import show
from bokeh.models import CustomJS, TextInput

text_input = TextInput(value="default", title="Label:")
text_input.js_on_change("value", CustomJS(code="""
    console.log('text_input: value=' + this.value, this.toString())
"""))

curdoc().add_root(text_input)
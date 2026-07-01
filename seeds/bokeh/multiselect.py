from bokeh.io import curdoc
from bokeh.io import show
from bokeh.models import CustomJS, MultiSelect

OPTIONS = [("1", "foo"), ("2", "bar"), ("3", "baz"), ("4", "quux")]

multi_select = MultiSelect(value=["1", "2"], options=OPTIONS)
multi_select.js_on_change("value", CustomJS(code="""
    console.log('multi_select: value=' + this.value, this.toString())
"""))

curdoc().add_root(multi_select)
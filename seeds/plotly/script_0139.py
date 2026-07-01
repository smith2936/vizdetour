import plotly.figure_factory as ff
import numpy as np

x1 = np.random.randn(200) - 1
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 1

hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']
colors = ['#835AF1', '#7FA6EE', '#B8F7D4']

# Create distplot with curve_type set to 'normal'
fig = ff.create_distplot(hist_data, group_labels, colors=colors, bin_size=.25,
                         show_curve=False)

# Add title
fig.update_layout(title_text='Hist and Rug Plot')
fig.show(renderer="json")
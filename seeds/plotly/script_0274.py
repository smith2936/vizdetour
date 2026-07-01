import plotly.figure_factory as ff
import numpy as np

x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']
colors = ['#393E46', '#2BCDC1', '#F66095']

fig = ff.create_distplot(hist_data, group_labels, colors=colors,
                         bin_size=[0.3, 0.2, 0.1], show_curve=False)

# Add title
fig.update(layout_title_text='Hist and Rug Plot')
fig.show(renderer="json")
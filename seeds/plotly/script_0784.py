import plotly.figure_factory as ff

data_matrix = [['Name', 'Equation'],
               ['Pythagorean Theorem', '$a^{2}+b^{2}=c^{2}$'],
               ['Euler\'s Formula', '$F-E+V=2$'],
               ['The Origin of Complex Numbers', '$i^{2}=-1$'],
               ['Einstein\'s Theory of Relativity', '$E=m c^{2}$']]

fig =  ff.create_table(data_matrix)
fig.show(renderer="json")
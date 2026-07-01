import plotly.figure_factory as ff
import numpy as np
Al, Cu = np.mgrid[0:1:7j, 0:1:7j]
Al, Cu = Al.ravel(), Cu.ravel()
mask = Al + Cu <= 1
Al, Cu = Al[mask], Cu[mask]
Y = 1 - Al - Cu

enthalpy = (Al - 0.5) * (Cu - 0.5) * (Y - 1)**2
fig = ff.create_ternary_contour(np.array([Al, Y, Cu]), enthalpy,
                                pole_labels=['Al', 'Y', 'Cu'],
                                ncontours=20,
                                coloring='lines',
                                showmarkers=True)
fig.show(renderer="json")
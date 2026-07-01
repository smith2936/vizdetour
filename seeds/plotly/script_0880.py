import plotly.express as px
import numpy as np
df = px.data.iris()
fig = px.scatter(df, x='petal_length', y='sepal_length', facet_col='species', color='species',
                 hover_data={'species':False, # remove species from hover data
                             'sepal_length':':.2f', # customize hover for column of y attribute
                             'petal_width':True, # add other column, default formatting
                             'sepal_width':':.2f', # add other column, customized formatting
                             # data not in dataframe, default formatting
                             'suppl_1': np.random.random(len(df)),
                             # data not in dataframe, customized formatting
                             'suppl_2': (':.3f', np.random.random(len(df)))
                            })
fig.update_layout(height=300)
fig.show(renderer="json")
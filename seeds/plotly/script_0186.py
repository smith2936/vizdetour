import pandas as pd
import numpy as np
pd.options.plotting.backend = "plotly"
np.random.seed(1)

df = pd.DataFrame(dict(
    a=np.random.normal(loc=1, scale=2, size=100),
    b=np.random.normal(loc=2, scale=1, size=100)
))
fig = df.plot.hist()
fig.show(renderer="json")
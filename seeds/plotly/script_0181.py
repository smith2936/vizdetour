import pandas as pd
pd.options.plotting.backend = "plotly"

df = pd.DataFrame(dict(a=[1,3,2], b=[3,2,1]))
fig = df.plot(title="Pandas Backend Example", template="simple_white",
              labels=dict(index="time", value="money", variable="option"))
fig.update_yaxes(tickprefix="$")
fig.show(renderer="json")
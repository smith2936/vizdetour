import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates

rng = np.random.default_rng(19680801)

fig, ax = plt.subplots(layout='constrained', figsize=(7, 4))

time = np.arange(np.datetime64('2020-01-01'), np.datetime64('2020-03-31'),
                 np.timedelta64(1, 'D'))

ax.plot(time, rng.random(size=len(time)))

ax.xaxis.set_major_formatter(mdates.DateFormatter('%d'))

sec = ax.secondary_xaxis(location=-0.075)
sec.xaxis.set_major_locator(mdates.MonthLocator(bymonthday=1))

sec.xaxis.set_major_formatter(mdates.DateFormatter('  %b'))
sec.tick_params('x', length=0)
sec.spines['bottom'].set_linewidth(0)

sec.set_xlabel('Dates (2020)')

plt.show()
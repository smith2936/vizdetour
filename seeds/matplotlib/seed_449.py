import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import matplotlib.dates as mdates

data = cbook.get_sample_data('goog.npz')['price_data']

fig, ax = plt.subplots(figsize=(6.4, 2.3), layout='constrained')

ax.plot('date', 'adj_close', data=data)

ax.xaxis.set_major_locator(mdates.MonthLocator(bymonth=(1, 7)))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
ax.grid(True)
ax.set_ylabel(r'Price [\$]')
ax.set_title('DefaultFormatter', loc='left', y=0.85, x=0.02, fontsize='medium')

plt.show()
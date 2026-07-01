import matplotlib.pyplot as plt
import numpy as np

import matplotlib.cbook as cbook
from matplotlib.ticker import Formatter


r = cbook.get_sample_data('goog.npz')['price_data']
r = r[:9]  


class MyFormatter(Formatter):
    def __init__(self, dates, fmt='%a'):
        self.dates = dates
        self.fmt = fmt

    def __call__(self, x, pos=0):
        try:
            return self.dates[round(x)].item().strftime(self.fmt)
        except IndexError:
            pass


fig, ax2 = plt.subplots(figsize=(6, 3))

ax2.plot(r["adj_close"], 'o-')

ax2.set_title("Plot y at Index Coordinates Using MyFormatter")
ax2.xaxis.set_major_formatter(MyFormatter(r["date"], '%a'))

plt.show()
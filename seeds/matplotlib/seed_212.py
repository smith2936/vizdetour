import matplotlib.pyplot as plt
import numpy as np

import matplotlib.cbook as cbook


r = cbook.get_sample_data('goog.npz')['price_data']
r = r[:9]  


def format_date(x, _):
    try:
        return r["date"][round(x)].item().strftime('%a')
    except IndexError:
        pass


fig, ax2 = plt.subplots(figsize=(6, 3))

ax2.plot(r["adj_close"], 'o-')

ax2.set_title("Plot y at Index Coordinates Using Custom Formatter")
ax2.xaxis.set_major_formatter(format_date)

plt.show()
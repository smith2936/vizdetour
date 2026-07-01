import matplotlib.pyplot as plt
import numpy as np

import matplotlib

matplotlib.rcParams['font.size'] = 8.0

np.random.seed(19680801)

data2 = np.random.gamma(4, size=[60, 50])
colors2 = 'black'
lineoffsets2 = 1
linelengths2 = 1

fig, ax = plt.subplots()
ax.eventplot(data2, colors=colors2, lineoffsets=lineoffsets2, linelengths=linelengths2)
plt.show()
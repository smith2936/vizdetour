import matplotlib.pyplot as plt
import numpy as np

import matplotlib

matplotlib.rcParams['font.size'] = 8.0

np.random.seed(19680801)

data1 = np.random.random([6, 50])
colors1 = [f'C{i}' for i in range(6)]
lineoffsets1 = [-15, -3, 1, 1.5, 6, 10]
linelengths1 = [5, 2, 1, 1, 3, 1.5]

fig, ax = plt.subplots()
ax.eventplot(data1, colors=colors1, lineoffsets=lineoffsets1, linelengths=linelengths1)
plt.show()
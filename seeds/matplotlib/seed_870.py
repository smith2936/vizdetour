import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 10)
y = x.reshape(-1, 1)
h = x * y

fig, (ax1, ax2) = plt.subplots(ncols=2)

ax1.set_title("origin='upper'")
ax2.set_title("origin='lower'")
ax1.contourf(h, levels=np.arange(5, 70, 5), extend='both', origin="upper")
ax2.contourf(h, levels=np.arange(5, 70, 5), extend='both', origin="lower")

plt.show()
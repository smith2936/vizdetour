import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0.1, 4, 0.5)
y = np.exp(-x)
error = 0.1 + 0.2 * x

lower_error = 0.4 * error
upper_error = error
asymmetric_error = [lower_error, upper_error]

fig, ax1 = plt.subplots()
ax1.errorbar(x, y, xerr=asymmetric_error, fmt='o')
ax1.set_title('variable, asymmetric error')
ax1.set_yscale('log')
plt.show()
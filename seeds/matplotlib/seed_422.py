import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)

people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos = np.arange(len(people))
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))

fig, ax = plt.subplots()

hbars = ax.barh(y_pos, performance, xerr=error, align='center')
ax.set_yticks(y_pos, labels=people)
ax.invert_yaxis()  
ax.set_xlabel('Performance')
ax.set_title('How fast do you want to go today?')

ax.bar_label(hbars, fmt='%.2f')
ax.set_xlim(right=15)  

plt.show()
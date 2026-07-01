import matplotlib.pyplot as plt

labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%.0f%%',
       textprops={'size': 'small'}, radius=0.5)
plt.show()
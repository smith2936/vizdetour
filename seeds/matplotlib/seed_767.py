import matplotlib.pyplot as plt

t = plt.title('Hi mom')
print('Text setters')
plt.setp(t)
print('Text getters')
plt.getp(t)
plt.show()
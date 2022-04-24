import matplotlib.pyplot as plt
import numpy as np

x1 = np.random.randint(1, 4, 4)
x2 = np.random.randint(4, 6, 30)
x3 = np.random.randint(6, 8, 44)
x4 = np.random.randint(8, 12, 8)
x5 = np.random.randint(12, 20, 1)


plt.hist(x1, bins=[1, 4], edgecolor = 'k', color = "indigo")
plt.hist(x2, bins=[4, 6], edgecolor = 'k', color = "indigo")
plt.hist(x3, bins=[6, 8], edgecolor = 'k', color = "indigo")
plt.hist(x4, bins=[8, 12], edgecolor = 'k', color = "indigo")
plt.hist(x5, bins=[12, 20], edgecolor = 'k', color = "indigo")

plt.xlabel('Number of letters')
plt.ylabel('Number of surnames')
plt.show()
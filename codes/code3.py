import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_excel('table3(2).xlsx')

x1 = list(df['C1'])
x2 = list(df['C2'])
x3 = list(df['C3'])
x4 = list(df['C4'])
x5 = list(df['C5'])


plt.hist(x1, bins=[1, 4], edgecolor = 'k', color = "indigo")
plt.hist(x2, bins=[4, 6], edgecolor = 'k', color = "indigo")
plt.hist(x3, bins=[6, 8], edgecolor = 'k', color = "indigo")
plt.hist(x4, bins=[8, 12], edgecolor = 'k', color = "indigo")
plt.hist(x5, bins=[12, 20], edgecolor = 'k', color = "indigo")

plt.xlabel('Number of letters')
plt.ylabel('Number of surnames')
plt.show()



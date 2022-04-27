#ICSE 2019,Class 12
#Question 3-A
#Verifying whether obtained x values are correct solutions or not for the given trigonometric equation

#Python libraries for math
import matplotlib.pyplot as plt
import numpy as np
import mpmath as mp

#LHS of the given equation
t = np.arange(-2, 2, 0.01)
z = np.arctan((t-1)/(t-2)) + np.arctan((t+1)/(t+2))

#RHS of the given equation
y = (np.pi)/4

#Solutions of x obtained
a = 1/2**(0.5)
b = -1/2**(0.5)

#Plotting the graphs and labelling
plt.ylim(-1.5,2)
plt.grid()
plt.axhline(y, color = 'blue')
plt.axvline(a, color = 'orange')
plt.axvline(b, color = 'green')
plt.plot(t, z, color = 'indigo', label = 'Plot of LHS of given equation')

p = [0.707, -0.707]
q = [0.785, 0.785]
plt.scatter(p, q, s = 100, marker = 'x', color = 'red')

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend(loc="upper left")

c = [1.5, 1.01, -0.39] 
d = [0.82, 1.5, 1.5]

annotations = ["y = π/4", "x = 1/√2", "x = -1/√2"]

for i, txt in enumerate(annotations):
     plt.annotate(txt, (c[i], d[i]), textcoords = "data", ha = 'center')
plt.show()
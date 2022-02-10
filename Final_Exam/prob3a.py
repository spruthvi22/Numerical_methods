import numpy as np 
import matplotlib.pyplot as plt

X, Y = np.loadtxt('data.txt', delimiter='  ', unpack=True)

plt.scatter(X,Y)
plt.xlabel('x')
plt.ylabel('y') 
plt.legend() 

plt.show()


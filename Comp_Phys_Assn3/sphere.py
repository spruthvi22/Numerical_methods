import numpy as np 
import matplotlib.pyplot as plt

x = np.random.rand(2, 1000000)

def f(x, y): 
    return x**2 + y**2 - 1

x_good = x[0][f(x[0], x[1]) < 0] 
y_good = x[1][f(x[0], x[1]) < 0]

sphere = 4*np.size(x_good)/1000000
print(sphere)
print(np.size(x_good))

#plt.scatter(x_good, y_good) 
#plt.show() 

x = np.random.rand(10, 10000000) 

def g(a, b, c, d, e, f, g, h, i, j): 
    return a**2 + b**2 + c**2 + d**2 + e**2 + f**2 + g**2 + h**2 + i**2 + j**2 - 1 

a_good = x[0][g(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9]) < 0] 
print(2**10*np.size(a_good)/10000000)



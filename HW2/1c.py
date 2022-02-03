import math
import numpy as np
import matplotlib.pyplot as plt


def f(x):
        return math.sin(math.cos(math.exp(x)))

def f_prime(x): 
    return -math.exp(x)*math.cos(math.cos(x))*math.sin(math.exp(x))

y = np.zeros(101)
y[0] = -1
for i in range(100): 
    y[i+1] = y[i] - f(y[i])/f_prime(y[i])

a = -1
b = 1
x = np.zeros(101)
x[0] = (a+b)/2

for i in range(100):
    if(f(a)*f(x[i])< 0):
        b = x[i]
        x[i+1] = (a+x[i])/2
    if(f(b)*f(x[i]) < 0):
        a = x[i] 
        x[i+1] = (x[i]+b)/2
    if(f(x[i]) == 0): 
        x[i+1] = x[i]

e1 = np.zeros(100)
e2 = np.zeros(100)
for i in range(100):
    e1[i] = x[i+1] - x[i] 
    e2[i] = y[i+1] - y[i] 

z = np.linspace(0,99,100)

plt.plot(z, e1, label='Bisection')
plt.plot(z, e2, label='Newton-Raphson') 

plt.xlabel("Iterations")
plt.ylabel("Error")

plt.legend()

plt.show()



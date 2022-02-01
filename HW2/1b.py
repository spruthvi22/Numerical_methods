import math
import numpy as np

def f(x):
        return math.sin(math.cos(math.exp(x)))

def f_prime(x): 
    return math.exp(x)*math.cos(math.cos(x))*math.sin(math.exp(x))

y = np.zeros(101)
y[0] = -1
for i in range(100): 
    y[i+1] = y[i] + f(y[i])/f_prime(y[i])

print(y)
print(y[100])



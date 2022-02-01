import math
import numpy as np 

def f(x): 
    return math.sin(math.cos(math.exp(x)))

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

print(x)
print(x[100])



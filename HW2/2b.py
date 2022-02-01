import numpy as np 
import math

def f(x): 
    return math.exp(x) 

x = np.linspace(0,1,101)
h = x[1] - x[0]
trapezoid = np.zeros(101) 

for i in range(100):
    trapezoid[i+1] = trapezoid[i] + 0.5*(f(x[i+1])+f(x[i]))*(x[i+1]-x[i])

simpson = h*(f(x[0]) + f(x[100]))/3 
for i in range(99):
    if(i%2 == 0):
        simpson = simpson + 4*h*f(x[i+1])/3 
    if(i%2 == 1): 
        simpson = simpson + 2*h*f(x[i+1])/3 


print(trapezoid[100])
print(simpson)

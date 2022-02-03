import numpy as np 
import math 
import scipy
from scipy import integrate

def f(x): 
    return math.exp(x)  

def vecf(x):
    y = np.zeros(len(x))
    for i in range(0,len(x)):
        y[i] = math.exp(x[i]) 
    return y
        
x = np.linspace(0,1,100)  
y = np.zeros(100) 
for i in range(100):
    y[i] = f(x[i]) 

trapezoid = np.trapz(y, x)
romberg = scipy.integrate.romberg(f, 0, 1)
simpson = scipy.integrate.simpson(y, x)
fixed_quad = scipy.integrate.fixed_quad(vecf, 0, 1)

print(trapezoid)
print(romberg)
print(simpson) 
print(fixed_quad)

import numpy as np 
import scipy
from scipy import integrate

def f(y): 
    return np.sqrt(2/3 - y**2) 

g = scipy.integrate.quad(f, -np.sqrt(2/3), np.sqrt(2/3))

print(g)
print(2*1.0471975511965983)
print(2*2.0943951023931966)
print(4*np.pi/3)

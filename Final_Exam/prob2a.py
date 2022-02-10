import numpy as np 
import scipy 
from scipy import integrate


def f(x): 
    return 2*np.sqrt(100-x**2)

A = scipy.integrate.quad(f, -10, 10)

print(A)

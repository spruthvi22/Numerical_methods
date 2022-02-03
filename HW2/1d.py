import numpy as np 
import math
import scipy
from scipy import optimize

def f(x):
        return math.sin(math.cos(math.exp(x)))

def f_prime(x): 
    return -math.exp(x)*math.cos(math.cos(x))*math.sin(math.exp(x))

bisect = scipy.optimize.bisect(f, -1, 1)
#newton = scipy.optimize.newton(f, -1, f_prime)

print(bisect)
#print(newton)


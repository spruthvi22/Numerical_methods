import numpy as np 
import scipy
from scipy import optimize 
from scipy import interpolate

X, Y = np.loadtxt('data.txt', delimiter='  ', unpack=True)

cs = scipy.interpolate.CubicSpline(X, Y) 

zero = scipy.optimize.bisect(cs, -1, 1) 

print(zero) 



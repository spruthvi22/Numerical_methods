import numpy as np 
import scipy
from scipy import interpolate 

x = np.array([0,1,2]) 
y = np.array([1,2,4]) 

cs = scipy.interpolate.CubicSpline(x, y) 

print('The interpolated value is: ')
print(cs(1.5))

print('The original value is: ')
print(2**1.5) 

print('The difference between the two is: ')
print(cs(1.5) - 2**1.5)


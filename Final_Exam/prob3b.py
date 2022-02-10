import numpy as np 
import scipy
from scipy import interpolate
import matplotlib.pyplot as plt

X, Y = np.loadtxt('data.txt', delimiter='  ', unpack=True)

cs = scipy.interpolate.CubicSpline(X, Y) 

plt.plot(X, cs(X)) 
plt.xlabel('x') 
plt.ylabel('Interpolated y') 
plt.legend()

plt.show() 


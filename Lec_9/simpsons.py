import numpy as np 

def f(x):
   return 10 - 3*x*x

x = np.linspace(-1,3,5)

A = (1/12)*(x[4]-x[0])*(f(x[0]) + f(x[4]) + 4*f(x[1]) + 2*f(x[2]) + 4*f(x[3]))

print(A)


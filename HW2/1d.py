import numpy as np
import scipy.optimize

def f(x):
    return np.sin(np.cos(np.exp(x)))

def fprime(x):
    return (-np.exp(x))*np.sin(np.exp(x))*np.cos(np.cos(np.exp(x)))

a=-1.0
b=1.0

xini=-1.0

print("Using Scipy.bisect",scipy.optimize.bisect(f,a,b))
print("Using Scipy.Newton",scipy.optimize.newton(f,xini,fprime))

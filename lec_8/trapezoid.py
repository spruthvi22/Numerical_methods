import numpy as np 

X = np.linspace(-2, 2, 1000) 
def f(x): 
    return(10 - x**2)

y = sum(f(X))

A = 4/len(X) * (y - 0.5*f(X[0]) - 0.5*f(X[999])) 
print(A)



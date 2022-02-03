#  Problem 1 (b). : Finding root using Newton-Raphson method.

import numpy as np

def f(x) :
    return np.sin(np.cos(np.exp(x)))

def df(x) :
    return -np.exp(x)*np.sin(np.exp(x))*np.cos(np.cos(np.exp(x)))

def main() :
    x=-1
    for i in range(100) :
        x=x-f(x)/df(x)
    print('The root is x =',x)

if __name__=="__main__" :
    main()

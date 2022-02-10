# Problem 1 (a). : Finding root using bisection method.

import numpy as np

def f(x) :
    return np.sin(np.cos(np.exp(x)))

def bisect(low,high) :
    mid=(high+low)/2
    if(f(high)*f(mid)<0) : return (mid,high)
    if(f(low)*f(mid)<0) : return (low,mid)

def main() :
    low,high=-1,1
    for i in range(100) : low,high=bisect(low,high)
    root=low if abs(f(low))<abs(f(high)) else high
    print('The root is x =',root)

if __name__=="__main__" :
    main()

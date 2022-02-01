# Problem 1 (c). : Plotting x_i-x_{i-1} bisection and Newton-Raphson methods.

import numpy as np
import matplotlib.pyplot as plt

def f(x) :
    return np.sin(np.cos(np.exp(x)))

def df(x) :
    return -np.exp(x)*np.sin(np.exp(x))*np.cos(np.cos(np.exp(x)))

def bisect(low,high) :
    mid=(high+low)/2
    if(f(high)*f(mid)<=0) : return (mid,high)
    if(f(low)*f(mid)<0) : return (low,mid)
    if(f(low)==0.0 or f(high)==0.0 or f(mid)==0) : return(low,high)

def main() :
    low,high,broot,prev=-1,1,0,0
    b_error=[]
    for i in range(10) :
        low,high=bisect(low,high)
        broot=low if (abs(f(low))<=abs(f(high))) else high
        b_error.append(broot-prev)
        prev=broot
    plt.plot(b_error,label='Error in Bisection Method')
    
    nroot,prev=-1,0
    n_error=[]
    for i in range(10) :
        nroot=nroot-f(nroot)/df(nroot)
        n_error.append(nroot-prev)
        prev=nroot
    plt.plot(n_error,label='Error in Newton-Raphson Method')

    plt.legend(loc='upper right')
    plt.xlabel('-- $i$ -->',fontsize=18)
    plt.ylabel('-- $x_i-x_{i-1}$ -->',fontsize=18)
    plt.title('Errors in Bisection and Newton-Raphson Methods',fontsize=20)
    plt.grid()
    plt.show()

if __name__=="__main__" :
    main()

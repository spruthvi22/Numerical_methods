# Problem 2 (b). : Integration using trapezoidal and Simpson's rules.

import numpy as np

def f(x) :
    return np.exp(x)

def main() :
    N=100
    dx=1/N
    trap_int,simp_int=0.0,0.0
    x=np.linspace(0,1,N)
    for i in range(1,N-1) :
        trap_int+=f(x[i])
    trap_int=dx*(trap_int+f(x[0])/2+f(x[-1])/2)
    
    N=101
    dx=1/N
    x=np.linspace(0,1,N)
    for i in range(1,N-1) :
        if i%2==0 : simp_int+=2*f(x[i])
        else : simp_int+=4*f(x[i])
    simp_int=(dx/3)*(simp_int+f(x[0])+f(x[-1]))

    print('The value found using the trapezoidal rule is I =',trap_int)
    print('The value found using Simpson\'s rule is I =',simp_int)

if __name__=="__main__" :
    main()

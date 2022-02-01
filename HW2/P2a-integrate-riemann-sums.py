# Problem 2 (a). : Integration using left-point, mid-point and right-point rules.

import numpy as np

def f(x) :
    return np.exp(x)

def main() :
    N=100
    dx=1/N
    print(dx)
    left_int,right_int,mid_int=0.0,0.0,0.0
    lefts=np.linspace(0,1-dx,N)
    rights=np.linspace(dx,1,N)
    mids=np.linspace(dx/2,1-dx/2,N)

    for i in range(N) :
        left_int+=f(lefts[i])*dx
        right_int+=f(rights[i])*dx
        mid_int+=f(mids[i])*dx
    
    print('The value found using the left-point rule is I =',left_int)
    print('The value found using the right-point rule is I =',right_int)
    print('The value found using the mid-point rule is I =',mid_int)
    print('The analytical value of the integral is I = e-1 =',np.exp(1)-1)

if __name__=="__main__" :
    main()

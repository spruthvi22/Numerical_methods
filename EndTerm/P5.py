# Problem 5

import numpy as np

def f(x,y) :
    return ((4-x**2-y**2)**(1/2))

def main() :
    # discretising the region of integration in analogy how a line is discretised in single integrals  
    N=100
    dx,dy=1/N,1/N
    integral=0.0
    x=np.linspace(-1+dx/2,1-dx/2,N)
    y=np.linspace(-1+dy/2,1-dy/2,N)
    # each (x[i],y[j]) represents the center of one of the squares making up the region of integration, so that the mid-point rule can be applied

    for i in range(N) :
        for j in range(N) :
            integral+=dx*dy*f(x[i],y[i]) # mid-point rule in action with area of the rectangle replaced by volume of the cuboid  

    print('\nThe value of the double integral found using midpoint is',integral)

if __name__=="__main__" :
    main()

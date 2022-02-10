# Problem 3

import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
from scipy import optimize

def main() :
    # part a. :  reads the data from data.txt and generates the required scatter plot
    data=np.loadtxt('data.txt')
    x=data[:,0]
    y=data[:,1]
    plt.scatter(x,y,label='Raw Data',color='black')
    
    # part b. : interpolates the data from data.txt and plot it as required
    interp=interpolate.CubicSpline(x,y)
    x_cont=np.linspace(min(x),max(x),200)
    plt.plot(x_cont,interp(x_cont),label='Interpolated Function',color='blue')
    
    plt.xlabel('-- x -->')
    plt.ylabel('-- y -->')
    plt.title('Plot of Data from data.txt')
    plt.grid()
    plt.legend(loc='upper right')
    plt.show()
    
    # part c. : finds the root of the interpolated function using bisection method and outputs it
    root=optimize.bisect(interp,-1,1)
    print('\nThe root found using bisection method is x =',root)

if __name__=="__main__" :
    main()

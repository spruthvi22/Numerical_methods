# Problem 1 (d). : Finding root using library methods scipy.optimize.bisect() and scipy.optimize.newton().

from scipy import optimize as opt
import numpy as np

def f(x) :
    return (np.sin(np.cos(np.exp(x))))

def df(x) :
    return -np.exp(x)*np.sin(np.exp(x))*np.cos(np.cos(np.exp(x)))

def main() :
    bisect=opt.bisect(f,-1,1)
    print('The root found using scipy.optimize.bisect() is x =',bisect)
    newton=opt.newton(f,-1,df)
    print('The root found using scipy.optimize.newton() is x =',newton)

if __name__=="__main__" :
    main()

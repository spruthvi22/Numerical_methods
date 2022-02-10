# Problem 2 (a). : Integration using numpy.trapz(), scipy.integrate.simpson(), scipy.integrate.romberg() and scipy.integrate.fixed_quad().

import numpy as np
from scipy import integrate

def f(x) :
    return np.exp(x)

def main() :
    N=100
    dx=1/N
    x=np.linspace(0,1,N)
    trap_int=np.trapz(f(x),x)
    simp_int=integrate.simpson(f(x),x)
    rom_int=integrate.romberg(f,0,1)
    quad_int=integrate.fixed_quad(f,0,1,n=5)

    print('The value found using numpy.trapz() is I =',trap_int)
    print('The value found using scipy.integrate.simpson() is I =',simp_int)
    print('The value found using scipy.integrate.romberg() is I =',rom_int)
    print('The value found using scipy.integrate.fixed_quad() is I =',quad_int[0])

if __name__=="__main__" :
    main()

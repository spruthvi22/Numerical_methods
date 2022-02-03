import numpy as np
import scipy.integrate

def f(x):
    return np.exp(x)

a=0.0
b=1.0
n=100
x=np.linspace(a,b,n)
dx=(b-a)/100
y=f(x)

trap=np.trapz(y,x,dx)
simp=scipy.integrate.simps(y,x,dx)
rom=scipy.integrate.romberg(f,a,b)
Gauss=scipy.integrate.fixed_quad(f,a,b)


print("Using Trapezoidal method",trap)
print("Using Simpson method",simp)
print("Using Romberg method",rom)
print("Using 5th order Gaussian quadrature method",Gauss)


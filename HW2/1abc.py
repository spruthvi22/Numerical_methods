import numpy as np
from matplotlib import pyplot as plt


def f(x):
    return np.sin(np.cos(np.exp(x)))

def fprime(x):
    return (-np.exp(x))*np.sin(np.exp(x))*np.cos(np.cos(np.exp(x)))

def bisec(f,itr):
    a=-1.0
    b=1.0
    c=a
    root=0.0
    for i in range(itr):
        c=(a+b)/2.0
        if (f(c)==0):
            break
        if (f(a)*f(c)<0):
            b=c
        else:
            a=c
    if (f(a)<f(b)):
        root=a
    else:
        root=b
    return root

def NewRaphBisec(f,itr):
    xmin=-1.0
    xmax=1.0
    x=xmin
    xnext=0.0
    c=0.0
    for i in range(itr):
        xnext=x-f(x)/fprime(x)
        if (xnext<xmin or xnext>xmax):
            c=(xmin+xmax)/2.0
            if (f(xmin)*f(c)<0):
                xmax=c
            else:
                xmin=c
            if (f(xmin)<f(xmax)):
                x=xmin
            else:
                x=xmax
        else:
            x=xnext
    return x

def Newton(f,itr):
    x=-1.0
    for i in range(itr):
        x=x-f(x)/fprime(x)
    return x


itera=100
print("Using Bisection",bisec(f,itera))
print("Using Newton",Newton(f,itera))
print("Using Newton+Bisection",NewRaphBisec(f,itera))


def error(method):
    roots=np.zeros(itera)

    for i in range(1,itera+1):
      roots[i-1]=method(f,i)
    errors=np.zeros(itera-1)
    for i in range(1,itera):
      errors[i-1]=abs(roots[i]-roots[i-1])
    return errors

iterations=np.linspace(2,itera,itera-1)

plt.yscale("log")
plt.plot(iterations,error(bisec), label="Bisection")
plt.plot(iterations,error(Newton), label="Newton-Raphson")
plt.xlabel("No. Of Iterations")
plt.ylabel("Error")
plt.title("Problem 1, Error vs Iterations")
plt.legend()

plt.show()






import numpy as np
from matplotlib import pyplot as plt


def f(x):
    return np.exp(x)

def left(f,itr):
    a=0.0
    b=1.0
    deltax=(b-a)/itr
    summ1=0.0
    x=a
    for i in range(1,itr+1):
        x=a+(i-1)*deltax
        summ1=summ1+f(x)*deltax
    return summ1

def right(f,itr):
    a=0.0
    b=1.0
    deltax=(b-a)/itr
    summ2=0.0
    x=a
    for i in range(1,itr+1):
        x=a+i*deltax
        summ2=summ2+f(x)*deltax
    return summ2


def mid(f,itr):
    a=0.0
    b=1.0
    deltax=(b-a)/itr
    summ3=0.0
    x=a
    for i in range(1,itr+1):
        x=a+(i-0.5)*deltax
        summ3=summ3+f(x)*deltax
    return summ3

def trape(f,itr):
    a=0.0
    b=1.0
    deltax=(b-a)/itr
    summ4=f(a)+f(b)
    x=a
    for i in range(1,itr):
        x=a+i*deltax
        summ4=summ4+2*f(x)
    summ4=summ4*(deltax/2)
    return summ4

def simpson(f,itr):
    a=0.0
    b=1.0
    deltax=(b-a)/itr
    summ5=f(a)+f(b)
    x=a+deltax
    for i in range(1,int(itr/2+1)):
        summ5=summ5+4*f(x)
        x=x+2*deltax
    x=a+2*deltax
    for j in range(1,int(itr/2)):
        summ5=summ5+2*f(x)
        x=x+2*deltax
    summ5=summ5*(deltax/3)
    return summ5

def error(intmethod):
    integral=np.zeros(100)
    eps=np.zeros(99)
    iterations=100
    for j in range(1,iterations+1):
        integral[j-1]=intmethod(f,j)
    for k in range(1,100):
        eps[k-1]=integral[k]-integral[k-1]
    return eps

integral=np.zeros(50)
errSimp=np.zeros(49)

exact=np.exp(1)-1

for j in range(1,51):
    integral[j-1]=simpson(f,2*j)
for k in range(1,50):
    errSimp[k-1]=integral[k]-integral[k-1]

print("using leftpoint",left(f,100))
print("using rightpoint", right(f,100))
print("using midpoint", mid(f,100))
print("deviation of left method from exact",abs(exact-left(f,100)))
print("deviation of right method from exact",abs(exact-right(f,100)))
print("deviation of mid method from exact",abs(exact-mid(f,100)))

print("using trapezoidal", trape(f,100))
print("using simpson", simpson(f,100))

itera=np.linspace(2,100,99)
iterSimp=np.linspace(2,100,49)

plt.plot(itera, error(left), label="Using Leftpoint")
plt.plot(itera, error(right), label="Using Rightpoint")
plt.plot(itera, error(mid), label="Using Midpoint")
plt.plot(itera, error(trape), label="using Trapezoidal")
plt.plot(iterSimp, errSimp, label="Using Simpson")

plt.xlabel("No. Of iterations")
plt.ylabel("Error")
plt.title("Problem 2, Error vs Iterations")
plt.legend()
plt.show()


import numpy as np 

x = np.linspace(0,2,3) 
y = 2**x

def L0(a):
    return (a - x[1])*(a-x[2])/((x[0]-x[1])*(x[0]-x[2])) 

def L1(a):
    return (a-x[0])*(a-x[2])/((x[1]-x[0])*(x[1]-x[2])) 

def L2(a):
    return (a-x[0])*(a-x[1])/((x[2]-x[0])*(x[2]-x[1])) 

def P(a): 
    return y[0]*L0(a) + y[1]*L1(a) + y[2]*L2(a) 

print(P(1.5)) 
print(2**(1.5))  
print("The difference is: ") 
print(P(1.5) - 2**(1.5)) 


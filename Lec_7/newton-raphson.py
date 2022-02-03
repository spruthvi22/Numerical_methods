import numpy as np 

def f(x) : return (x**2 - 10)
def f_prime(x) : return (2*x) 

x = 0.01; 

for i in range(1, 100): 
    x = x - (f(x)/f_prime(x))

print (x)








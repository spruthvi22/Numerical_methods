import numpy as np 
import math

def f(x): 
    return math.exp(x) 

x = np.linspace(0,1,100) 

left_point = 0 

for i in range(99):
    left_point = left_point + f(x[i])*(x[i+1]-x[i]) 

right_point = 0 
for i in range(99): 
    right_point = right_point + f(x[i+1])*(x[i+1] - x[i])

mid_point = 0 
for i in range(99):
    mid_point = mid_point + f(0.5*(x[i+1]+x[i]))*(x[i+1]- x[i])  


print('From left-point rule: ')
print(left_point)
print('From right-point rule: ') 
print(right_point)
print('From mid-point rule:')
print(mid_point) 
print(np.exp(1)-1)

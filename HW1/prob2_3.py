import numpy as np
def max(x):
    m=x[0]
    for i in range (0,len(x)):
        if(m<x[i]):
            m=x[i]
    return m
y=[10,20,4,152,89,23,1200,56,-9,-1000,301020,9]
x=np.array(y)
print("The largest number is: ", max(x))


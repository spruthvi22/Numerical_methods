import numpy as np
def max(x,N):
    for i in range (0,N):
        m=x[i]
        for j in range (i,len(x)):
            if(m<x[j]):
                x[i]=x[j]
                x[j]=m
                m=x[i]
    return x[0:N]

y=[12,13,162,876,-987,53426,12,45,-9]
x=np.array(y)
Z=int(input("Enter the number of values required: "))
print(max(x,Z))

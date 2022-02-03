import numpy as np
import time

def fibo(n):
    temp1=0
    temp2=1
    for i in range(n-1):
        term=temp1+temp2
        temp1=temp2
        temp2=term
    print(term)
    
n=int(input("enter value of n: "))
start=time.time()
fibo(n)
stop=time.time()
reqtime=stop-start
print(reqtime)





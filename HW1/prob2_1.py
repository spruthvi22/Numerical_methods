import numpy as np
array=[10,32,2,54,100,24,1,33]
p=len(array)

def sorting(arr,i):
    for j in range(i+1,p):
        if arr[i] < arr[j]:
            arr[i],arr[j]=arr[j],arr[i]
    arr_1=arr
    return arr_1

n=int(input("Give the value of n: ")) 
semisort=array
for i in range(n):
    semisort=sorting(semisort,i)
#semisort=sorting(semisort,0)
for i in range(n):
    print(semisort[i])


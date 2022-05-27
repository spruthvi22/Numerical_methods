import numpy as np 
import matplotlib.pyplot as plt
import time

a = 1664525
c = 1013904223
m = 2**32 

X = np.zeros(10000)
X[0] = 1
start = time.time()
for i in range(9999): 
    X[i+1] = ((a*X[i] + c)%m)

Y = X/m 
end = time.time()
 
plt.hist(Y, density = True)
plt.show()
print(end - start)

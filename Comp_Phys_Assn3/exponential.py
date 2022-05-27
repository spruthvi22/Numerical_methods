import numpy as np 
import matplotlib.pyplot as plt

x = np.random.rand(10000)
x0 = np.linspace(0,7,7000)
def y(x): 
    return -np.log(x)/2

plt.plot(x0, 2*np.exp(-2*x0)) 
plt.hist(y(x), bins = 100, density = True) 
plt.show()

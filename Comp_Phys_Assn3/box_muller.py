import numpy as np 
import matplotlib.pyplot as plt

x1 = np.random.rand(10000)
x2 = np.random.rand(10000) 

y1 = np.sqrt(-2*np.log(x1))*np.cos(2*np.pi*x2) 
y2 = np.sqrt(-2*np.log(x1))*np.sin(2*np.pi*x2)

x = np.linspace(-4, 4, 10000) 
def f(x): 
    return np.exp(-x**2/2)/np.sqrt(2*np.pi) 

plt.plot(x, f(x))
plt.hist(y1, bins = 100, density = True)
plt.show()

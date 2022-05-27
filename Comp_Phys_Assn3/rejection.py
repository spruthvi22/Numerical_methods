import numpy as np 
import matplotlib.pyplot as plt 

x = np.random.default_rng().uniform(0, 3, 100000)
y = np.random.default_rng().uniform(0, 1, 100000) 

def f(x): 
    return np.sqrt(2/np.pi)*np.exp(-x**2/2) 

x1 = np.linspace(0, 3, 10000) 
x_good = x[y < f(x)] 
y_good = y[y < f(x)]

#plt.scatter(x_good, y_good) 
plt.plot(x1, f(x1))
plt.hist(x_good, bins = 100, density = True)
plt.show() 


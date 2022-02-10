import numpy as np 
#import scipy
#from scipy import integrate
import matplotlib.pyplot as plt

def A(r): 
    return np.pi*r**2

r = np.linspace(5,50,10)
y = A(r) 

plt.plot(r, y) 
plt.xlabel("Radius of circle") 
plt.ylabel("Area of circle") 
plt.legend() 

plt.show()


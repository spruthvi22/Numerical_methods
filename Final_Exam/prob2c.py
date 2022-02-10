import numpy as np 
import scipy
from scipy import interpolate
import matplotlib.pyplot as plt

def A(r): 
    return np.pi*r**2

r = np.linspace(5,50,10)
y = A(r) 

cs = scipy.interpolate.CubicSpline(r, y) 

r1 = np.array([5,10,13,15,20,25,30,35,40,45,50])
y1 = cs(r1) 

plt.plot(r,y, label = "Without interpolation")
plt.plot(r1, y1, label = "With interpolation") 
plt.xlabel("Radius of circle") 
plt.ylabel("Area of circle") 
plt.legend() 

plt.show()

print(cs(13)) 

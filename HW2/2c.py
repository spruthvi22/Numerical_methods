import numpy as np 
import scipy
from scipy import integrate
import matplotlib.pyplot as plt


trapz = np.zeros(102)
simpson = np.zeros(102)
left_point = np.zeros(102)
right_point = np.zeros(102)
mid_point = np.zeros(102) 
for i in range(102): 
    x = np.linspace(0,1,i+1)
    y = np.exp(x) 
    trapz[i] = np.trapz(y, x) 
    simpson[i] = scipy.integrate.simpson(y, x)
    l = 0
    r = 0 
    m = 0
    for j in range(i):
        l = l + np.exp(x[j])*(x[j+1] - x[j])  
        r = r + np.exp(x[j+1])*(x[j+1] - x[j]) 
        m = m + np.exp((x[j]+x[j+1])/2)*(x[j+1] - x[j])
    left_point[i] = l 
    right_point[i] = r
    mid_point[i] = m 



e1 = np.zeros(100) 
e2 = np.zeros(100)
e3 = np.zeros(100)
e4 = np.zeros(100)
e5 = np.zeros(100)
for i in range(100): 
    e1[i] = left_point[i+2] - left_point[i+1] 
    e2[i] = right_point[i+2] - right_point[i+1]
    e3[i] = mid_point[i+2] - mid_point[i+1] 
    e4[i] = trapz[i+2] - trapz[i+1]  
    e5[i] = simpson[i+2] - simpson[i+1]

x = np.linspace(1,100,100)

plt.plot(x, e1, label = 'Left-Point') 
plt.plot(x, e2, label = 'Right-Point')
plt.plot(x, e3, label = 'Mid-Point')
plt.plot(x, e4, label = 'Trapezoid')
plt.plot(x, e5, label = 'Simpson') 

plt.xlabel('Iterations') 
plt.ylabel('Integral') 


plt.legend()
plt.show()


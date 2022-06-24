import numpy as np 
import matplotlib.pyplot as plt

V4 = np.array([1114, 1215, 1338, 1490, 1578]) 
fold3 = np.array([1595, 1454, 1589, 1530, 1383]) 
fold4 = np.array([11, 20, 571, 1521, 1378]) 

rate = fold4/fold3 

plt.plot(V4, rate)
plt.xlabel("V4") 
plt.ylabel("Ratio of 4-fold to 3-fold") 
plt.show() 

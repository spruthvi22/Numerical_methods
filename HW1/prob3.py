import matplotlib.pyplot as plt
import numpy as np
t=np.linspace(0,2*np.pi,1000)
x1=np.sin(t)
y1=np.cos(t)
plt.plot(x1,y1,label="a")
x2=np.cos(3*t)
y2=np.sin(2*t)
plt.plot(x2,y2,label="b")
x3=np.abs(np.cos(4*t))*np.cos(t)
y3=np.abs(np.cos(4*t))*np.sin(t)
plt.plot(x3,y3,label="c")
plt.legend()
plt.show()


import numpy as np
import matplotlib.pyplot as plt

t=np.linspace(0,2*np.pi,1000)

x1=np.cos(t)
y1=np.sin(t)

x2=np.cos(3*t)
y2=np.sin(2*t)

x3=abs(np.cos(4*t))*np.cos(t)
y3=abs(np.cos(4*t))*np.sin(t)

plt.plot(x1,y1,label='a')
plt.plot(x2,y2,label='b')
plt.plot(x3,y3,label='c')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Parametric Plot')
plt.legend()
plt.show()


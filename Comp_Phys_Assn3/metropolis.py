import numpy as np 
import matplotlib.pyplot as plt

def f(x): 
    if(3 < x < 7): 
        return 1
    else:
        return 0 
steps = 100000

theta = np.zeros(steps) 
theta[0] = 4
for i in range(steps-1):
    theta_prime = np.random.normal(loc=theta[i], scale = 1)
    r = np.random.rand(1) 
    if(f(theta_prime)/f(theta[i]) > r): 
        theta[i+1] = theta_prime 
    else: 
        theta[i+1] = theta[i] 
ax = np.linspace(1, steps, steps)

plt.hist(theta, density = True)
plt.show()

plt.plot(ax, theta)
plt.show() 

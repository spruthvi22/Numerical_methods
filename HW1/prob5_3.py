import matplotlib.pyplot as plt
import numpy as np
mu=0
sigma=1.0
x=np.random.normal(mu,sigma,1000)
y=np.random.rand(1000)
plt.subplot(1,2,1)
plt.hist(x,20,range=(-2.0,2.0),density=True)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Histogram of 1000 normally distributed random numbers")

plt.subplot(1,2,2)
plt.hist(y, 20, density=True)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Histogram of 1000 Random Numbers")

plt.suptitle("Histogram using Pyplot")
plt.show()

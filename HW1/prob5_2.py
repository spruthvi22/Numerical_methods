import matplotlib.pyplot as plt
import numpy as np
mu, sigma= 0,1.0
s=np.random.normal(mu, sigma, 1000)
n_bins=25
plt.hist(s,n_bins, range=(-2.0,2.0), density=True)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Histogram of 1000 numbers of normal Distribution")
plt.show()

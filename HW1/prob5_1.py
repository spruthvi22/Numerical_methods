import numpy as np
import matplotlib.pyplot as plt
s=np.random.rand(1000)
plt.hist(s,20,density=True)
plt.xlabel("X-axis")
plt.ylabel("Yaxis")
plt.title("Histogram of 1000 Random Numbers")
plt.show()


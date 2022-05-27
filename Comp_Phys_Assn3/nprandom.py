import numpy as np 
import matplotlib.pyplot as plt
import time

start_time = time.time()
X = np.random.rand(10000)
end_time = time.time()

plt.hist(X, density = True)
plt.show() 
print(end_time - start_time)

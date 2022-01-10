import numpy as np
import matplotlib.pyplot as plt

fig, ax=plt.subplots(1,2)
n_bins=20
x=np.random.rand(1000)

y=np.random.normal(0.0,1.0,1000)

ax[0].hist(x, bins=n_bins)
ax[0].set_xlabel('range of values')
ax[0].set_ylabel('number of points in a given range')
ax[0].set_title('Random distribution')

ax[1].hist(y, range=[-2.0,2.0])
ax[1].set_xlabel('range of values')
ax[1].set_ylabel('number of points in a given range')
ax[1].set_title('Normal distribution')

plt.show()


import numpy as np 
import scipy
from scipy import stats

N1 = np.array([4, 10, 10, 13, 20, 18, 18, 11, 13, 14, 13]) 
N2 = np.array([3, 7, 11, 15, 19, 24, 21, 17, 13, 9, 5]) 

n = np.array([4, 8, 12, 16, 20, 24, 20, 16, 12, 8 ,4])

chi2_1 = 0 
chi2_2 = 0 
for i in range(11): 
    chi2_1 = chi2_1 + (N1[i] - n[i])**2/n[i] 
    chi2_2 = chi2_2 + (N2[i]-n[i])**2/n[i] 

p1 = 1 - scipy.stats.chi2.cdf(chi2_1, 10)
p2 = 1 - scipy.stats.chi2.cdf(chi2_2, 10) 

print(p1)
print(p2)

import numpy as np 
import emcee
from scipy.optimize import minimize
import corner
import matplotlib.pyplot as plt

x = np.array([201, 244, 47, 287, 203, 58, 210, 202, 198, 158, 165, 201, 157, 131, 166, 160, 186, 125, 218, 146])
y = np.array([592, 401, 583, 402, 495, 173, 479, 504, 510, 416, 393, 442, 317, 311, 400, 337, 423, 334, 533, 344])
yerr = np.array([61, 25, 38, 15, 21, 15, 27, 14, 30, 16, 14, 25, 52, 16, 34, 31, 42, 26, 16, 22])

def log_likelihood(theta, x, y, yerr): # We'll define the negative log-likelihood. 
    a, b, c = theta
    model = a*x**2 + b*x + c
    sigma2 = yerr**2
    return 0.5*np.sum((y-model)**2/sigma2 + np.log(2*np.pi*sigma2))

guess = (1.0, 1.0, 1.0) 
soln = minimize(log_likelihood, guess, args=(x,y,yerr)) 

def log_prior(theta):
    a, b, c = theta
    if -0.1 < a < 0 and 0 < b < 5  and 15 < c < 20: 
        return 0 
    return -np.inf

def log_probability(theta, x, y, yerr): 
    lp = log_prior(theta) 
    if not np.isfinite(lp):
        return -np.inf 
    return lp - log_likelihood(theta, x, y, yerr) 

nwalkers, ndim = 50, 3 
pos = soln.x + 1e-4 * np.random.rand(nwalkers, ndim)

sampler = emcee.EnsembleSampler(
        nwalkers, ndim, log_probability, args=(x,y,yerr)
)
sampler.run_mcmc(pos, 4000) 

samples = sampler.get_chain()
plt.plot(samples[:,:,0])
plt.show()
plt.plot(samples[:,:,1])
plt.show()
plt.plot(samples[:,:,2]) 
plt.show()

medians = np.median(np.median(samples,axis=0), axis=0)
a_true, b_true, c_true = medians
labels = ["a","b","c"]
flat_samples = sampler.get_chain(flat=True)
fig = corner.corner(
        flat_samples, labels=labels, truths=[a_true, b_true, c_true]
);
plt.show()

inds = np.random.randint(len(flat_samples), size = 200) 
x0 = np.linspace(0,250,250000) 
for ind in inds:
    sample = flat_samples[ind] 
    plt.plot(x0, np.dot(np.vander(x0, 2), sample[:2]), "C1", alpha=0.3) 
plt.errorbar(x, y, yerr=yerr, fmt=".k", capsize=0)
plt.plot(x0, a_true*x0**2 + b_true*x0 + c_true, "k", label="truth") 
plt.legend(fontsize=14)
plt.xlim(0,250)
plt.xlabel("x")
plt.ylabel("y") 
plt.show()

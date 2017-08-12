import numpy as np
n, p = 10,.5 # number of trials, probability of each trial

s = np.random.binomial(n, p, 100)
print(s)
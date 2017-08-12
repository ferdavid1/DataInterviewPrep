import matplotlib.pyplot as plt
import numpy as np

mu, sigma = 0,1
s = np.random.normal(mu, sigma, 500)
count, bins, ignored = plt.hist(s, 50, normed=True)
plt.plot(bins, 1/(sigma*np.sqrt(2*np.pi))*np.exp(-(bins-mu)**2/(2*sigma**2)), linewidth=2, color='r')
plt.show()
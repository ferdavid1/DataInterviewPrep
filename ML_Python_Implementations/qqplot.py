import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

measurements = np.random.normal(loc=40, scale=10, size=80)
stats.probplot(measurements, dist='norm', plot=plt)
plt.show()
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

df = pd.DataFrame(np.random.rand(10,5), columns=['A', 'B', 'C', 'D', 'E'])
df.plot(kind='box')
plt.show()
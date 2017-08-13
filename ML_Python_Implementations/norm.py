from numpy import linalg as LA
import numpy as np
a = np.arange(22)
# print(a)
print(LA.norm(a))
print(LA.norm(a,1))
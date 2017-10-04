import numpy as np
a = np.random.randn(5) # pretend this is the output of a neural net
expa = np.exp(a) #exponentiate 
answer = expa /expa.sum()
print(answer.sum()) #if these are really probabilities, they will add to 1

A = np.random.randn(100, 5) # in reality, you dont get one array - this here is a 100 x 5 array
expA = np.exp(A)
answer = expA / expA.sum(axis=1, keepdims=True) # you have to sum across all columns, across dimensions
print(answer.sum(axis=1)) # should be 1 for every column

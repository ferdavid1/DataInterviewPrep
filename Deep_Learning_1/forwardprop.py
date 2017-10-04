# Creating an entire neural net from scratch in NumPy
import numpy as np 
import matplotlib.pyplot as plt 

Nclass = 500 # number of classification options

X1 = np.random.randn(Nclass, 2) + np.array([0, -2]) # create a gaussian cloud
X2 = np.random.randn(Nclass, 2) + np.array([2,2]) # second gaussian cloud
X3 = np.random.randn(Nclass, 2) + np.array([-2,2]) # third gaussian cloud
X = np.vstack([X1, X2, X3]) # vector stacking of gaussian clouds

Y = np.array([0]*Nclass + [1]*Nclass + [2]*Nclass) # create out labels of 0,1,2 -- Non binary classification
plt.scatter(X[:,0], X[:,1], c=Y, s=100, alpha=0.5)
plt.show()

D = 2 # input dimension
M = 3 # hidden layer size
K = 3 # number of classes

W1 = np.random.rand(D, M) # weight 1
b1 = np.random.randn(M) # bias 1
W2 = np.random.randn(M, K) # weight 2
b2 = np.random.randn(K) # bias 2

def forward(X, W1, b1, W2, b2): # FF neural network -- inputs: array, weights and biases
	Z = 1/(1+ np.exp(-X.dot(W1)-b1)) # sigmoid nonlinearity for the hidden layer 1 -- value of the hidden layer
	A = Z.dot(W2) +b2 # softmax of Z with second weights
	expA = np.exp(A) # exponentiate A
	Y = expA / expA.sum(axis=1, keepdims=True) # softmax'd output probabilities
	return Y

def classification_rate(Y, P): # same as accuracy - input: NN outputs, probabilities
	n_correct = 0 # initialize
	n_total = 0 #initialize
	for i in range(len(Y)):
		n_total += 1
		if Y[i] == P[i]:
			n_correct +=1
	return float(n_correct/n_total)

P_Y_given_X = forward(X, W1, b1, W2, b2) 
P = np.argmax(P_Y_given_X, axis=1) # the argmax returns the probabilities

assert(len(P) == len(Y)) # avoids different length errors

print("Classification Rate/ Accuracy :", classification_rate(Y, P)) # labels, probabilities
# Classification Rate/ Accuracy : 0.3333333333333333 -- As expected, it does about chance
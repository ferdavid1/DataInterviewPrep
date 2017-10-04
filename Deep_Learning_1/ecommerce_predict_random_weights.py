import numpy as np 
from ecommerce_preprocess import get_data

X, Y = get_data()

M = 5 # hidden units
D = X.shape[1]
K = len(set(Y)) # number of predicting categories

W1 = np.random.rand(D, M) # weight 1
b1 = np.random.randn(M) # bias 1
W2 = np.random.randn(M, K) # weight 2
b2 = np.random.randn(K) # bias 2

def softmax(a):
	expA = np.exp(a)
	return expA /expA.sum(axis =1, keepdims=True)

def forward(X, W1, b1, W2, b2):
	Z = np.tanh(X.dot(W1) + b1) # use the tanh activation function instead of sigmoidal to get hidden layer values
	return softmax(Z.dot(W2) + b2)

P_Y_given_X = forward(X, W1, b1, W2, b2)
predictions = np.argmax(P_Y_given_X, axis=1)

def classification_rate(P, Y):
	return np.mean(Y == P)

print("Score: ", classification_rate(Y, predictions))

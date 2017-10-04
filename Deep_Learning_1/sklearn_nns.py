from sklearn.neural_network import MLPClassifier
# that is a multilayer perceptron neural network classifier

#http://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html
'''
Parameters:

	hidden_layer_sizes:  tuple, length = n_layers - 2, default (100,)

	activation: {‘identity’, ‘logistic’, ‘tanh’, ‘relu’}, default ‘relu’
		Activation function for the hidden layer.
		‘identity’, no-op activation, useful to implement linear bottleneck, returns f(x) = x
		‘logistic’, the logistic sigmoid function, returns f(x) = 1 / (1 + exp(-x)).
		‘tanh’, the hyperbolic tan function, returns f(x) = tanh(x).
		‘relu’, the rectified linear unit function, returns f(x) = max(0, x)

	solver : {‘lbfgs’, ‘sgd’, ‘adam’}, default ‘adam’
		The solver for weight optimization.
		‘lbfgs’ is an optimizer in the family of quasi-Newton methods.
		‘sgd’ refers to stochastic gradient descent.
		‘adam’ refers to a stochastic gradient-based optimizer proposed by Kingma, Diederik, and Jimmy Ba

	Note: The default solver ‘adam’ works pretty well on relatively 
	large datasets (with thousands of training samples or more) 
	in terms of both training time and validation score. For small datasets,
	however, ‘lbfgs’ can converge faster and perform better.

	alpha : float, optional, default 0.0001	
		L2 penalty (regularization term) parameter.

	batch_size : int, optional, default ‘auto’
		Size of minibatches for stochastic optimizers. 
		If the solver is ‘lbfgs’, the classifier will not use minibatch. 
		When set to “auto”, batch_size=min(200, n_samples)

	learning_rate : {‘constant’, ‘invscaling’, ‘adaptive’}, default ‘constant’
		Learning rate schedule for weight updates.
		‘constant’ is a constant learning rate given by ‘learning_rate_init’.
		‘invscaling’ gradually decreases the learning rate learning_rate_ at each time step ‘t’ using an inverse scaling exponent of ‘power_t’. effective_learning_rate = learning_rate_init / pow(t, power_t)
		‘adaptive’ keeps the learning rate constant to ‘learning_rate_init’ as long as training loss keeps decreasing. Each time two consecutive epochs fail to decrease training loss by at least tol, or fail to increase validation score by at least tol if ‘early_stopping’ is on, the current learning rate is divided by 5.
		Only used when solver='sgd'.

	etc
'''
from ecommerce_preprocess import get_data
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X,Y = get_data()
Xtrain, Xtest, Ytrain, Ytest = train_test_split(X, Y, test_size=0.25, random_state=0)

model = MLPClassifier(hidden_layer_sizes=(30,30), activation='tanh', solver='sgd',learning_rate='adaptive', learning_rate_init=0.05, max_iter=2000)

model.fit(Xtrain, Ytrain)
train_accuracy = model.score(Xtrain, Ytrain)
test_accuracy = model.score(Xtest, Ytest)
print("training: {}\n Testing: {}".format(train_accuracy, test_accuracy))
# https://thuijskens.github.io/2016/12/29/bayesian-optimisation/
import sklearn.gaussian_process as gp

def bayesian_opt(n_iters, sample_loss, xp, yp):
	'''
	N_iters: int - number of iterations to run the algorithm for
	sample_loss: function
	xp: array-like shape=[n_samples, n_params]. Array of previously evaluated hyperparameters
	yp: Array-like, shape = [n_samples, 1]. Array of values of sample_loss for the hyperparameters in 'xp'
	'''
	kernel = gp.kernels.Matern()
	model = gp.GaussianProcessRegressor(kernel=kernel, alpha= 1e-4, n_restarts_optimizer=10, normalize_y=True)
	for i in range(n_iters):
	    # update our belief of the loss function
	    model.fit(xp, yp)

	    # sample_next_hyperparameter is a method that computes the argmax of the acquistion function
	    next_sample = sample_next_hyperparameter(model, yp)

	    # Evaluate the loss for the new hyperparameters
	    next_loss = sample_loss(next_sample)

	    # update xp and yp

from sklearn.datasets import make_classification
data, target = make_classification(n_samples=2500, n_features=45, n_informative=15, n_redundant=5)

# We'll optimize the penalization parameter C, and kernel parameter gamma (y), of a support Vector machine, with the RBF kernel. T
# the loss function we'll use is the cross-validated area under the curve (AUC), based on three fold. 

from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC 

def sample_loss(params):
	C = params[0]
	gamma = params[1]

	#Sample C and gamma on the log-uniform scale
	model = SVC(C=10 **C, gamma=10**gamma, random_state=12345)

	# sample parameters on a log scale 
	return cross_val_score(model, X=data, y=target, scoring='roc_auc', cv=3).mean()

if __name__ == '__main__':
	bayesian_opt(5, sample_loss([0.1, 5]), [2500,5], [2500] )
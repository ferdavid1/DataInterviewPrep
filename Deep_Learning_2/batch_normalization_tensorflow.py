import tensorflow as tf

#training vs testing batch norm 

# when training, use mean = batch_mean, var = batch_var
# when testing, use mean = training set mean, var = training set var
# so you need to calculate batch mean, batch variance, running mean, running variance yourself
	# yike tensorflow sucks 

batch_normalization = tf.nn.batch_normalization
def forward(X, training=True):
	a = X.dot(W) # no bias 
	if training:
		batch_mean, batch_var = tf.nn.moments(a, [0])
		out = batch_normalization(a, batch_mean, batch_var, beta, gamma)
	else:
		# running mean and running variance
		out = batch_normalization(a, running_mean, running_var, beta, gamma)
	return f(out)
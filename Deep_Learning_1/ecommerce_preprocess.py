import pandas as pd 
import numpy as np 

# df = pd.read_csv('ecommerce_data.csv')
# print(df.head())
#    is_mobile  n_products_viewed  visit_duration  is_returning_visitor  \
# 0          1                  0        0.657510                     0   
# 1          1                  1        0.568571                     0   
# 2          1                  0        0.042246                     1   
# 3          1                  1        1.659793                     1   
# 4          0                  1        2.014745                     1   

#    time_of_day  user_action  
# 0            3            0  
# 1            2            1  
# 2            1            0  
# 3            1            2  
# 4            1            2 

def get_data():
	
	df = pd.read_csv('ecommerce_data.csv')
	data = df.as_matrix()

	X = data[:, :-1] # X is everything until the last column, which is Y
	Y = data[:,-1]

	X[:,1] = (X[:,1] - X[:1].mean()) / X[:,1].std() # normalize the numerical columns
	X[:,2] = (X[:,2] - X[:2].mean()) / X[:,2].std() # normalize the numerical columns

	N, D = X.shape
	X2 = np.zeros((N, D+3))
	X2[:,0:(D-1)] = X[:,0:(D-1)]

	for n in range(N): # basically one hot encoding manually
		t = int(X[n, D-1])  # get time of day
		X2[n,t+D-1] = 1
	return X2, Y

def get_binary_data():
	X,Y = get_data()
	X2 = X[Y <= 1]
	Y2 = Y[Y <= 1]

	return X2, Y2

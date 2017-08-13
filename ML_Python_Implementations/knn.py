import numpy as np
import matplotlib.pyplot as plt 
def dist(p0, p1):
	return np.sum((p0-p1)**2) # Euclidean distance

def knn(training, trainingLabels, newPoint):
	dists = np.array([dist(t, newPoint) for t in training])
	nearest = dists.argmin()
	return trainingLabels[nearest]

training = np.random.rand(300, 1)
trainingLabels = training
newPoint = 0.301
print(knn(training, trainingLabels, newPoint))


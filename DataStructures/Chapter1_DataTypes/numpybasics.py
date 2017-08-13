import numpy as np
import time

x = np.array( ((11,12,13), (21,22,23), (31,32,33)))
print (x)
x1 = np.array( ((11,12,13), (21,22,23)))
print(x.ndim) #ndim tells us the number of dimensions of an array

def testing_numpy():
	ax = np.array([1,2,3])
	ay = np.array([3,4,5])
	print(ax)
	print(ax*2)
	print(ax+10)
	print(np.sqrt(ax))
	print(np.cos(ax))
	print(ax-ay)
	print(np.where(ax<2, ax, 10))
	m = np.matrix([ax,ay,ax])
	print(m)
	print(m.T)
	grid1 = np.zeros(shape=(10,10), dtype = float)
	grid2 = np.ones(shape=(10,10), dtype = float)
	print(grid1)
	print(grid2)
	print(grid1[1]+10)
	print(grid2[:,2]*2)

def trad_version(): #this is how you would do things with reg. lists
	t1 = time.time()
	X = range(10000000)
	Y = range(10000000)
	Z = []
	for i in range(len(X)):
		Z.append(X[i]+Y[i])
	return time.time() - t1

def numpy_version(): # this is how you would do the same in numpy
	t1 = time.time()
	X = np.arange(10000000)
	Y = np.arange(10000000)
	Z = X + Y
	return time.time() - t1

if __name__ == '__main__':
	assert(trad_version() > 3.0)
	assert(numpy_version() < 0.1)
	testing_numpy()
	print(trad_version())
	print(numpy_version())

import ctypes

class M(object):
	def public(self):
		print('Use tab to see me')
	def _private(self):
		print("You won't be able to Tab to see me")

m = M()
m.public()
m._private()

class DynamicArray(object):
	'''
	DYNAMIC ARRAY CLASS (Similar to Python list)
	'''
	def __init__(self):
		self.n = 0 # count actual elements (default is 0)
		self.capacity = 1 # Default capacity
		self.A = self.make_array(self.capacity)

	def __len__(self):
		'''
		Return number of elements sorted in array
		'''
		return self.n 

	def __getitem__(self, k):
		'''
		Return element at index k
		'''
		if not 0 <= k < self.n:
			return IndexError('K is out of bounds!')
		return self.A[k]

	def append(self, ele):

		if self.n == self.capacity:
			self._resize(2*self.capacity) # 2x if capacity isnt enough

		self.A[self.n] = ele 
		self.n += 1

	def _resize(self, new_cap):
		
		B = self.make_array(new_cap) 

		for k in range(self.n):
			B[k] = self.A[k]

		self.A = B 
		self.capacity = new_cap

	def make_array(s, new_cap):

		return (new_cap * ctypes.py_object)()

arr = DynamicArray()

arr.append(1)
print(len(arr))

arr.append(2)
print(arr[1])




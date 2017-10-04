# Create cache for known results
factorial_memo = {}

def factorial(k):

	if k < 2: # base case, because this is recursive
		return 1 

	if not k in factorial_memo:
		factorial_memo[k] = k * factorial(k-1)

	return factorial_memo[k]

print(factorial(12), factorial_memo)

# We are using the dictionary to keep track of old results!

# You could probably also use a tuple for this

class Memoize:

	def __init__(self, f): # f for function
		self.f = f 
		self.memo = {}

	def __call__(self, *args):
		if not args in self.memo:
			self.memo[args] = self.f(*args)
		return self.memo[args]

factor = Memoize(factorial)
print(factor)
# in functions, the three laws of recursion are:
	# 1. It must have a base case
	# 2. It must change its state and move towards the base case
	# 3. It must call itself, recursively

# For every recursive call, the recursive function has to allocate memory on the 'stack' for arguments, return adress, and local variables
	# it costs time to push and pop these data onto the stack
# Recursive algorithms take at least O(n) space where n is the depth of the recursive call
# Recursion is very costly when there are duplicated calculations and/or there are overlap among subproblems
# In some cases this can cause the stack to overflow
# For this reason, when subproblems overlap, iterative solutions are faster

# Recursive Relations
# to describe the running time of recursive functions, we use recursive relations:
	# T(n) = a * T(g(n)) + f(n), 
		# where a represents the number of recursive calls,
		# g(n) is the size of each subproblem to be solved recursively,
		# and f(n) is any extra work done in the function. 

# Divide and Conquer Algorithms
# recurrences for the divide and conquer algorithms have the form:
	# T(n) = a * T(n/b) + f(n)
		# where a is the recursive calls, 
		# each with a percent 1/b of the dataset
		# the algorithm does f(n) of wok

# If an algorithm does not have any recursive calling, we only need to analyze its data structures and flow blocks.
# in this case, complexities of code blocks executed one after the other are just added,
	# and complexities of nested loops are multiplied
	# THE ABOVE TWO LINES ARE IMPORTANT!
# If an algorithm has recursive calls, we can use the recursive functions defined in the previous section to find the runtime
	# When we write a recurrence relation for a function, we mus write two equations:
		# one for the general case 
		# one for the base case (that should be O(1), so that T(1) = 1)
# for instance, the algorithm to find the nth element in a Fibonacci sequence (which is known to be exponential):

def find_fibonacci_seq_rec(n):
	if n < 2: return n
	return find_fibonacci_seq_rec(n-1) + find_fibonacci_seq_rec(n - 2)
print(find_fibonacci_seq_rec(8))

# here, g(n)s (the size of each subproblem) is n-2 and n-1, 
	# a is 2, 
	# f(n) is 1 (the if statement)
# so the recursive relation is (for the first recursion):
	# T(n) = 2T(n-1) + 1
# for the second recursion:
	# T(n) = 2T(n-2) + 1
# for k recursions:
	# T(n) = 2^kT(n-k) + k
# we need to make the base case (T(1) = 1) be O(1),
# so since the base case k is 0, the only thing that needs to be 1 is n-k
# thus n-k=1 m k = n - 1
# and further, T(n) = 2^n-1 + n-2 = 2^n, which is exponential

# Table of runtime results for several algorithms
'''
------------------------------------------------------------------------------------------------------------------------
O(n^2) quadratic	|	insertion, slection sort
O(n ln n) loglinear	|	algos breaking problems into smaller chunks per invocation, then sticking the results together
					|	quick and merge sort
O(n) 	linear		|	Iteration over a list
O(ln n) log			|	Algorithms breaking problem into smaller chunks per invocation (without remerging)
					|	Searching a binary search tree
O(1) constant		|	hash table lookup/modification
O(n^k)	polynomial	|	k-nested loops over n
O(k^n)  exponential |   producing every subset of n items
O(n!)   factorial   |   producing every ordering of n values
------------------------------------------------------------------------------------------------------------------------
'''

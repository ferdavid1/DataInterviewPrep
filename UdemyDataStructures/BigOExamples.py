# O(1) Constant
def func_constant(values):
	print(values[0])

lst = [1,2,3]
# the algo is constant, because even if the list is infinite, it only returns the first value

# O(n) Linear
def func_list(lst):
	for val in lst:
		print(val)
# n is linear to however many values you have

# O(n^2) Quadratic
def func_quad(lst):
	for item1 in lst:
		for item2 in lst:
			print(item1, item2)
# for every iteration, you're accessing n twice, so n*n 

# We only care about the biggest elements, so 2n = n, n+1 = n, etc

def print2(lst):
	for val in lst:
		print(val)
	for val in lst:
		print(val)
# this is 2n, which is the same as n

def comp(lst):
	print(lst[0]) # O(1)
	midpoint = len(lst)/2 # O(n/2)
	for val in lst[:int(midpoint)]:
		print(val)
	for x in range(10): # O(10)
		print('hello world')

# O(1) + O(n/2) + O(10) = O(n/2 + 11) = O(n)

def matcher(lst, match):
	for item in lst:
		if item == match:
			return True
	return False
#matcher(lst, 1) is O(1) --- Best case
#matcher(lst, 11) O(n) --- Worst case

# Space Complexity
def create_list(n):
	new_list = []
	for num in range(n):
		new_list.append('new')
	return new_list
# size of the new_list object size is relative to n
# O(n) space complexity

def printer(n):
	for x in range(n):
		print('hello world')
# O(n) time complexity
# O(1) = space complexity, because only 'hello world' is being printer every time



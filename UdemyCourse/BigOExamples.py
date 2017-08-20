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
comp(lst)
# O(1) + O(n/2) + O(10) = O(n/2 + 11) = O(n)


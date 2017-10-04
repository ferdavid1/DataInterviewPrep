'''
Write a recursive function which takes an integer and
computes the cumulative sum of 0 to that integer
'''

def cumsum(i):

	if i==0: # base case
		return 0

	return i + cumsum(i-1)

print(cumsum(4))

'''
Given an integer, create a function which returns the sum of
all the individual digits in that integer. 
For example, if n=4321, return 4+3+2+1
'''

def int_sum(i):
	# this one's hard
	# we need to think of it in terms of modulo
	# Ex: 4321/10 = 432.1, 432/10 = 43.2, 43/10 = 4.3
		# Means that 4321%10 = 1, 432%10=2, etc
	i = int(i)
	if i/10 < 0.1: # base case - first digit is at minimum 1 and 1/10 is 0.1
		return 0
	return i%10 + int_sum(i/10)

print(int_sum(438721))
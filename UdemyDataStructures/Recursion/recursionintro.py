# Factorial in recursive solution
def fact(n):

	if n==0: # base case
		return 1
	return n * fact(n-1)

print(fact(5))
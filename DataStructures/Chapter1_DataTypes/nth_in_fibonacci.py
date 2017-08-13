#recursive method, O(2^n)
def fib_rec(n):
	print ('''
	>>>fib_rec(2)
	1
	>>>fib_rec(5)
	5
	>>>fib_rec(7)
	13
	''')
	if n < 3:
		return 1
	return fib_rec(n-1) + fib_rec(n-2)
print (fib_rec(5))
z = '{name} has been {action}'
print (z.format(name = '"Fibonacci"', action = 'decoded'))
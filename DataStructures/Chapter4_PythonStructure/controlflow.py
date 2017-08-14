# the if statement (ughhh)
'''
Python Style Guide:
	 - Never use == or != to compare singletons, such as 'None'.
	 	- use 'is' or 'is not' instead
	 - Beware of writing 'if x' when you mean 'if x is not None'
	 -- Instead of 'if len(x) == 0', use 'if not x' --
	 -- Yield vs Return:
	 	- yield is like return for generator functions instead of iterator functions.
	 		- generator function values are returned one at a time, by calling __next__() until StopIteration is called
	 	- Fibonacci with generators:
	 		- def fib_generator():
	 			a,b = 0,1
	 			while True:
	 				yield b
	 				a, b = b, a+b
	 		- if __name__ == '__main__':
	 			fib = fib_generator()
	 			print(next(fib))
	 			print(next(fib))
	 			print(next(fib))
	 -- Break vs Continue:
	 	- 'break' breaks out of the smallest enclosing for or while loops
	 	- 'continue' continues with the next iteration of the loop

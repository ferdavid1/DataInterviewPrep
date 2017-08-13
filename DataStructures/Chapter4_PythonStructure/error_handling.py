# there are two kinds of errors when we compile a program:
	# syntax errors (parsing errors)
	# exceptions (errors detected during executions, not unconditionally fatal)
		# try, except, finally
		# we can use 'else' with try and except, to respond to ther others outside of the except
		# else:
			for arg in sys.argv[1:]:
				try:
					f = open(arg, 'r') #opening a file from command line argument
				except IOError:
					print('cannot open', arg)
				else:
					print(arg, 'has', len(f.readlines()), 'lines')
					f.close()
		# use the 'as' statement:
			try:
				raise Error 
			except Error as error:
				pass
			
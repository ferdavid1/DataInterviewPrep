# writing good functions

# GOOD
def foo(a, b= None):
	if b is None:
		b = []

# BAD
def foo(a, b=[]):
	pass

# python -c 'import some_module'

# if __name__ = '__main__' is used when it is a standalone script, and not something to be called from another script (imported functions)

# Byte-coded Compiled Modules (.pyc files)
	# how to make one? run python xxxx.py -O
	# this optimizes the code
	# this also makes it harder to reverse engineer it

# sys
'''
sys.path is a list of strings that determines the interpreters search path from modules
basically the PYTHONPATH for modules (often anaconda2/lib/site-packages for you dude)

----- Sys.argv -----
allows for the recovery of arguments passed in the command line
Ex: '''
import sys

'''print command line arguments'''
for arg in sys.argv[1:]:
	print(arg)

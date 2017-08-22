# Lists
'''
In Python, lists are dynamic arrays and support a number
of common operations through methods called on them. 
The two most common operations are indexing, and assigning to an index position
These operations were designed to be run in constant time, O(1)
'''
def method1():
	l = []
	for n in range(10000):
		l = l + [n]

def method2():
	l = []
	for n in range(10000):
		l.append(n)

def method():
	l = [n for n in range(10000)]

def method4():
	l = list(range(10000))

# these are all the same process, in order from slowest to fastest.

# Dictionaries
'''
Implementations of hash tables
'''
d = {'k1':1, 'k2':2}
print(d['k1'])

'''
Getting and setting items in a dictionary is also O(1).
'''

# decorator pattern - @ symbol
	# a tool to elegantly specify some transformation of functions and methods
	# it allows you to wrap an object that provides some core functionality with other objects that alter that functionality
	# a normal object:
'''
class NiceClass(object):
 	def method(self):
 		method = my_decorator(method)

# can be written as:

class NiceClass(object):
	@ my_decorator
	def method(self):
		something else
'''
# real life example:
'''
def sum(func):
	s = 0
	for i in func():
		s += i
	return s

def iterate():
	a = []
	for i in range(10):
		a.append(i)
	return a
print(sum(iterate))

	# instead of this above, with decorators:
@sum
def integrate():
	a = []
	for i in range(10):
		a.append(i)
	return a
print(integrate)
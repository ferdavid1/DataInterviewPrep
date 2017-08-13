'''
A linked list is a linear list of nodes,in general containing a value and a pointer (reference)
to the next node (and sometimes to the previous node).

The last node in a linked list has a None reference
'''
class Node(object):
	
	def __init__(self, value=None, pointer=None):
		self.value = value
		self.pointer = pointer

	def getData(self):
		return self.value

	
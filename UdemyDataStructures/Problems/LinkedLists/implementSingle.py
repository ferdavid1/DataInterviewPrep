'''
Create a node class and show how it can be used to create
a Singly Linked List
'''
class Node(object):

	def __init__(self, value):
		self.value = value
		self.nextnode = None

if __name__ == '__main__':
	a = Node(1)
	b = Node(2)
	c = Node(3)
	
	a.nextnode = b
	b.nextnode = c

	print(a.nextnode.nextnode.value)
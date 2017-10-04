'''
Pros and Cons of linked lists
Pros:
	
	Linked lists have constant-time O(1) insertions and deletions in any position.
	In comparison, arrays require O(n) time to do the same thing

	Linked lists can continue to expand without having to specify their size ahead of time

Cons:

	To access an element in a linked list, you need to take O(k) time to go from the head of the list to the kth element
	In Contrast, arrays have constant time operations to access elements in an array
'''

class Node(object): # takes in object, returns pointer

	def __init__(self, value):
		self.value = value
		self.nextnode = None # initialized from the tail of the LL

if __name__ == '__main__':
	a = Node(1)
	b = Node(2)
	c = Node(3)
	a.nextnode = b
	b.nextnode = c
	print(a.value, a.nextnode.value)
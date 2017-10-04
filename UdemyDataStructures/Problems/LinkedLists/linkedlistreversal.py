'''
Write a function to reverse a Linked List in place.
The function will take in the head of the list as input,
and return the new head of the list.
Singly linked or doubly linked??? 
Assuming singly linked
Assuming not a circular linked list
'''
class Node(object):

	def __init__(self, value):
		self.value = value
		self.nextnode = None

def reverse(head):
	curr_node = head
	previous = None
	nextnode = None
	while curr_node: # while is not None
		nextnode = curr_node.nextnode # next is real next
		curr_node.nextnode = previous # real next is previous
		previous = curr_node # previous is current 
		curr_node = nextnode # current is next
	return previous # returns current head (not curr_node) because that would return the next

if __name__ == '__main__':
	
	# Create a list of 4 nodes
	a = Node(1)
	b = Node(2)
	c = Node(3)
	d = Node(4)

	# Set up order a,b,c,d with values 1,2,3,4
	a.nextnode = b
	b.nextnode = c
	c.nextnode = d

	print(reverse(a))
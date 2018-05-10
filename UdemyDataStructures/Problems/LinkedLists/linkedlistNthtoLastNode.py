'''
Write a function that takes a head node and an integer value
n, and returns the nth to last node in the linked list.
'''

class Node(object):

	def __init__(self, value):
		self.value = value
		self.nextnode = None

def Nth(val, head):
	node_list = []
	curr_node = head
	while curr_node: # traverse the linked list 
		node_list.append(curr_node)
		curr_node = curr_node.nextnode
	return node_list[-val]

if __name__ == '__main__':
	"""
	RUN THIS CELL TO TEST YOUR SOLUTION AGAINST A TEST CASE 

	PLEASE NOTE THIS IS JUST ONE CASE
	"""

	from nose.tools import assert_equal

	a = Node(1)
	b = Node(2)
	c = Node(3)
	d = Node(4)
	e = Node(5)

	a.nextnode = b
	b.nextnode = c
	c.nextnode = d
	d.nextnode = e

	####

	class TestNLast(object):
	    
	    def test(self,sol):
	        
	        assert_equal(sol(2,a),d)
	        assert_equal(sol(1,b),e)
	        assert_equal(sol(3,b),c)
	        print ('ALL TEST CASES PASSED')
	        
	# Run tests
	t = TestNLast()
	t.test(Nth)
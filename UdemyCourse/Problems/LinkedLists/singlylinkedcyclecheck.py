'''
Given a singly linked list, write a function which takes in the first
node in a singly linked list and returns a boolean indicating
if the linked list contains a "cycle"

A cycle is when a node's next point actually points back to 
a previous node in the list. This is also sometimes known
as a circularly linked list.
'''
class Node(object):

	def __init__(self, value):
		self.value = value
		self.nextnode = None # no previous node bc linked 

def isCycle(firstnode):
	# this would be the case if you know that the list contains 3 elements only
	# return firstnode.nextnode.nextnode.nextnode == firstnode
	curr_node = firstnode
	while curr_node.nextnode is not None:
		curr_node = curr_node.nextnode
		if curr_node == firstnode:
			return True
	return False

if __name__ == '__main__':
	
	"""
	RUN THIS CELL TO TEST YOUR SOLUTION
	"""
	from nose.tools import assert_equal

	# CREATE CYCLE LIST
	a = Node(1)
	b = Node(2)
	c = Node(3)

	a.nextnode = b
	b.nextnode = c
	c.nextnode = a # Cycle Here!


	# CREATE NON CYCLE LIST
	x = Node(1)
	y = Node(2)
	z = Node(3)

	x.nextnode = y
	y.nextnode = z

	# CREATE CYCLE LIST OF MORE THAN 3 ELEMENTS
	h = Node(1)
	i = Node(2)
	j = Node(3)
	k = Node(4)

	h.nextnode = i
	i.nextnode = j
	j.nextnode = k
	k.nextnode = h
	#############
	class TestCycleCheck(object):
	    
	    def test(self,sol):
	        assert_equal(sol(a),True)
	        assert_equal(sol(x),False)
	        assert_equal(sol(h), True)
	        
	        print("ALL TEST CASES PASSED")

	t = TestCycleCheck()
	t.test(isCycle)
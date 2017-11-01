'''
Given a binary tree of integers, print it in level
order. The output will contain space between the
numbers in the same level, and the new line between
different levels
'''
from tree_traversal_class import BinaryTree

class Node:

	def __init__(self, val=None):
		self.left = None
		self.right = None
		self.val = val

import collections
d = collections.deque([1,2,3])

def levelOrderPrint(tree):
	
	if not tree:
		return 

	nodes = collections.deque([tree]) # nodes as deque
	currentCount = 1
	nextcount = 0

	while nodes:
		currentNode = nodes.popleft() # collections function
		currentCount -= 1
		
		print(currentNode.val)

		if currentNode.left:
			nodes.append(currentNode.left)
			nextcount += 1

		if currentNode.right:
			nodes.append(currentNode.right)
			nextcount += 1

		if currentCount == 0:
			print('\n')
			currentCount, nextcount = nextcount, currentCount


if __name__ == '__main__':
	
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)

	levelOrderPrint(root)
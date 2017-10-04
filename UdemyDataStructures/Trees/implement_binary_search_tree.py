
'''
A Binary Search tree relies on the fact property that keys that are less than the parent are found in the left subtree,
and keys that are greater than the parent are found in the right subtree.

We will call this the 'bst' property

As we implement the map (mapping keys to values) interface, the bst property will guide us

This BST property holds for every parent and child in each subtree

For the example tree 70, 31, 93, 94, 14, 23, 73:

	Since 70 was the first key inserted into the tree, it is the root.
	
	Next, 31 is less than 70, so it goes into the tree as the left child of 70

	93 is greater than 90, so it goes in as the right child of 70
	
	94 is greater than 93, so it becomes the right child of 90. 

	14 is less than 31, so it goes in as a child of 31.

	23 is less than 31, but greater than 14, so it becomes a right child of 14.  (because this whole thing is recursive)

	73 is less than 93, so it becomes the left child of 93

To implement to the binary search tree, we will use the nodes and references approach similar to for linked lists.

But because we are also dealing with a tree, we will have a tree class like the previous in this section 

	thus, node class and tree class

The first class will be BinarySearchTree, and the second will be the TreeNode class

'''

class TreeNode(object):

	def __init__(self, key, val, left=None, right=None, parent=None):
		self.key = key
		self.payload = val
		self.leftChild = left
		self.rightChild = right
		self.parent = parent

	def hasLeftChild(self):
		return self.leftChild

	def hasRightChild(self):
		return self.rightChild

	def isLeftChild(self):
		return self.parent and self.parent.leftChild == self

	def isRightChild(self):
		return self.parent and self.parent.rightChild == self

	def isRoot(self):
		return not self.parent

	def isLeaf(self):
		return not (self.rightChild or self.leftChild)

	def hasAnyChildren(self):
		return self.rightChild or self.leftChild

	def hasBothCHildren(self):
		return self.rightChild and self.leftChild

	def replaceNodeData(self, key, value, lc, rc):
		self.key = key
		self.payload = value 
		self.leftChild = lc 
		self.rightChild = rc 
		if self.hasLeftChild():
			self.leftChild.parent = self
		if self.hasRightChild():
			self.rightChild.parent = self



class BinarySearchTree:

	def __init__(self):
		self.root = None
		self.size = 0

	def length(self):
		return self.size

	def __len__(self): # allows you to use the len command on your bst
		return self.size

	def __iter__(self): # allows you to iterate throught the bst
		return self.root.__iter__()

	def put(self, key, val):
		if self.root:
			self._put(key, val, self.root)
		else:
			self.root = TreeNode(key, val)
		self.size = self.size + 1

	def _put(self, key, val, currentNode):
		



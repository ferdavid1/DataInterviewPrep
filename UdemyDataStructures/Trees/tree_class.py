'''
In this case we will define a class that has attributes
for the root value, as well as the left and right subtrees.

Since this representation more closely follows the OOP
paradigm, we will continue to use this representation
for the remainder of this section
'''
class BinaryTree(object):

	def __init__(self, root):
		self.key = root
		self.leftchild = None
		self.rightchild = None

	def insertLeft(self, newNode):
		if not self.leftchild: # each subtree is a tree
			self.leftchild = BinaryTree(newNode) # new tree
		else:
			t = BinaryTree(newNode)
			t.leftchild = self.leftchild # leftchild object
			self.leftchild = t # set as a new tree

	def insertRight(self, newNode):
		if not self.rightchild:
			self.rightchild = BinaryTree(newNode)
		else:
			t = BinaryTree(newNode)
			t.rightchild = self.rightchild
			self.rightchild = t

	def setRootVal(self, newVal):
		self.key = newVal

	def getRootVal(self):
		return self.key

	def getLeftChild(self):
		return self.leftchild

	def getRightChild(self):
		return self.rightchild

if __name__ == '__main__':
	r = BinaryTree('a')
	r.insertLeft('b')
	r.insertRight('c')
	print(r.getLeftChild().getRootVal())
	print(r.getRightChild().getRootVal())
	r.setRootVal('1')
	print(r.getRootVal())
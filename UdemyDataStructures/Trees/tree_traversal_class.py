
class BinaryTree(object):

	def __init__(self, root):
		self.key = root
		self.LeftChild = None
		self.RightChild = None

	def insertLeft(self, val):
		if not self.LeftChild:
			self.LeftChild = BinaryTree(val)
		else:
			t = BinaryTree(val)
			t.LeftChild = self.LeftChild
			self.LeftChild = t 

	def insertRight(self, val):
		if not self.RightChild:
			self.RightChild = BinaryTree(val)
		else:
			t = BinaryTree(val)
			t.RightChild = self.RightChild
			self.RightChild = t

	def getRootValue(self):
		return self.key

	def setRootValue(self, val):
		self.key = val 

	def getLeftChild(self):
		return self.LeftChild

	def getRightChild(self):
		return self.RightChild

def preorder(tree): # root, then left, then right
	if tree: # base case
		print(tree.getRootValue())
		preorder(tree.getLeftChild())
		preorder(tree.getRightChild())

def inorder(tree):
	if tree:
		inorder(tree.getLeftChild())
		print(tree.getRootValue())
		inorder(tree.getRightChild())

def postorder(tree):
	if tree:
		inorder(tree.getLeftChild())
		inorder(tree.getRightChild())
		print(tree.getRootValue())

if __name__ == '__main__':
	r = BinaryTree(1)
	r.insertLeft(2)
	r.insertRight(3)
	r.getRightChild()
	r.getLeftChild()

	preorder(r)
	print('-----')
	inorder(r)
	print('-----')
	postorder(r)
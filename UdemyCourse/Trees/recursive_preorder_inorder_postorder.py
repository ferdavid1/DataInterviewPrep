
def preorder(tree): # root, then left, then right
	if tree: # base case
		print(tree.getRootVal())
		preorder(tree.getLeftChild())
		preorder(tree.getRightChild())

def inorder(tree):
	if tree:
		inorder(tree.getLeftChild())
		print(tree.getRootVal())
		inorder(tree.getRightChild())

def postorder(tree):
	if tree:
		inorder(tree.getLeftChild())
		inorder(tree.getRightChild())
		print(tree.getRootVal())


def preorder(tree): # root, then left, then right
	if tree: # base case
		print(tree.getRootVal())
		preorder(tree.getLeftChild)
		preorder(tree.getRightChild)


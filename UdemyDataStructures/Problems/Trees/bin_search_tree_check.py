# Given a binary tree, check whether it's a binary
# search tree or not
from tree_traversal_class import BinaryTree

values = []
def inorder(tree):
	if tree:
		inorder(tree.getLeftChild())
		values.append(tree.getRootValue())
		inorder(tree.getRightChild())

def sort_tree(vals):
	return vals == sorted(vals)

if __name__ == '__main__':
	r = BinaryTree(10)
	r.insertLeft(2)
	r.insertRight(30)

	inorder(r)
	print(sorted(values) == values)



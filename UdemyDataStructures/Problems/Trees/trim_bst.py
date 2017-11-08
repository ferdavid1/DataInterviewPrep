'''
Given the root of a binary search tree and 2 numbers min and max, 
trim the tree such that all the numbers in the new tree are between min and max (inclusive).
The resulting tree should still be a valid binary search tree. 
'''
from tree_traversal_class import BinaryTree, preorder
def trimBST(tree, minVal, maxVal):

	if not tree:
		return 

	tree.left = trimBST(tree.left, minVal, maxVal)
	tree.right = trimBST(tree.right, minVal, maxVal)

	if minVal <= tree.val <= maxVal:
		return tree

	if tree.val < minVal:
		return tree.right

	if tree.val > maxVal:
		return tree.left
	# print(tree.getLeftChild())
	# print(tree.getRightChild())
	# print(tree.getRootValue())

	
if __name__ == '__main__':
	minVal = 3
	maxVal = 8
	t = BinaryTree(2)
	t.insertLeft(4)
	t.insertRight(6)

	trimBST(t, minVal, maxVal)
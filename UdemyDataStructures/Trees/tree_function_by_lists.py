def BinaryTree(r):
	return [r, [], []]

def insertLeft(root, newBranch):
	t = root.pop(1) # remove the second element of the binary
	#tree and replace it with this new branch
	if len(t) > 1: # if a new left branch has already been inserted
		root.insert(1, [newBranch,t,[]]) #because t is not empty [] 
	else: # tree has an empty or only one left element
		root.insert(1, [newBranch, [], []])
	return root

def insertRight(root, newBranch):
	t = root.pop(2)
	if len(t) > 1:
		root.insert(2, [newBranch, [], t])
	else:
		root.insert(2, [newBranch, [], []])
	return root

def setRootVal(root, newVal):
	root[0] = newVal

def getLeftChild(root):
	return root[1]

def getRightChild(root):
	return root[2]
# def getRootVal(root):
# 	return root[0]

# def getLeftLeafVal(root, leaf):
# 	return root[1][leaf]

# def getRightLeafVal(root, leaf):
# 	return root[2][leaf]


if __name__ == '__main__':
	
	mytree = BinaryTree('a')
	insertLeft(mytree, 'b')
	insertLeft(mytree, 'd')
	insertLeft(mytree, 'e')
	insertRight(mytree, 'c')
	insertRight(mytree, 'f')
	l = getLeftChild(mytree)
	r = getRightChild(mytree)
	# print(getLeftLeafVal(mytree, 0))
	# print(getRighttLeafVal(mytree, 0))
	setRootVal(l, 'g')
	print(l)


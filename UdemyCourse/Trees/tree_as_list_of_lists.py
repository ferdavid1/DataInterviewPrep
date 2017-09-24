'''
In a list of lists tree, we will store the value of the root
node as the first element of the list.

The second element of the list will itself be a list
that represents the left subtree.

The third element of the list will be another list
that represents the right subtree
'''
# Implemented as a family tree
tree = ['a', #root
	['b', #left subtree
	['d', [], []],
	['e', [], []] ],
		['c', #right subtree
		['f', [], []],
		[] ]
	]
print('List of lists implementation: \n{}'.format(tree))
print('\nTree Visual:')
print('''
			a
		   / \ 
		  b   c
		 / \  |
		d   e f
''')

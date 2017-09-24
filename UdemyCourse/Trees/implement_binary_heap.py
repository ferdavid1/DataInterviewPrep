'''
Implementing a (min) binary heap for a priority queue.
In a min heap, the smallest value is always at the front.

BinaryHeap() creates a new, empty binary heap
insert(k) adds a new item to the heap
findMin() returns the item with the minimum key value
delMin() returns the item with the minimum key value
isEmpty() returns true if the heap is empty, false otherwise
size() returns the length of the heap
buildHeap(list) builds a new heap from a list of keys
'''

'''
A balanced binary tree has roughly the same number of nodes
in the left and right subtrees of the root.

In our heap implementation we keep the tree balanced by 
creating a complete binary tree.

A complete binary tree is a tree in which each level has
all of its nodes
'''

'''
The indices of a parent (P)'s children in a complete binary
heap are 2P and 2P+1
			  
   				  5
			    /   \
			   /  	 \
			  9		  11
			 / \ 	 /  \
			14  18	19   21
		   / |   |
		  33 17	27

[0, 5, 9, 11, 14, 18, 19, 21, 33, 17, 27]

Ex: children of node 9
	2(9) = 18 --> child 1
  2(9)+1 = 19 --> child 2
'''

class BinaryHeap(object):

	def __init__(self):
		self.lst = [0] # because we start with the 0 ind
		self.currentsize = 0

	# if the newly added item is less than its parent, 
	# then we can swap the item with its parent.
	# do this forever until its in the proper place
	def percUp(self, i):
		while (i // 2) > 0:
			if self.lst[i] < self.lst[i//2]:
				tmp = self.lst[i//2] # save parent
				self.lst[i//2] = self.lst[i] # parent is curr
				self.lst[i] = tmp # curr = parent
			i = i//2

	def insert(self, k):
		
	def percDown(self, i):
		pass
	def isEmpty(self):
		return self.lst == []

	def size(self):
		return len(self.lst)

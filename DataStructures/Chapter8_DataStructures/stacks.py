# A stack is a linear data structure that can be accessed only at one of its ends
	# (we refer to the end we can access as the top)
	# for either storing or retrieving
# you can think of a stack as a huge pile of books on your desk

# Array access of elements in a stack is restricted since a stack is a last-in-first out (LIFO) structure
	# However, stacks have the following operations running at O(1):
		# push: Insert an item at the top of the stack
		# pop: remove an item from the top of the stack
		# top/peek: look up the element on the top
		# empty/size: Check whether the stack is empty or return its size

# stacks in Python can be implemented with lists and the methods append() and pop()

class Stack(object):
	
	def __init__(self):
		self.content = []
		self.min_array = []
		self.min = float('inf') # infinity (positive upper bound)

	def push(self, value):
		if value < self.min:
			self.min = value # if the value is less than the maximum (infinity), set that as the minimum
		self.content.append(value)
		self.min_array.append(self.min)

	def pop(self):
		if self.content: # if the list is not empty
			value = self.content.pop() # no index specified means it removes and returns the last item in the list
			self.min_array.pop()
			if self.min_array:
				self.min = self.min_array[-1]
			return value
		else:
			return 'Empty List. ' 

	def find_min(self):
		if self.min_array:
			return self.min_array[-1]
		else:
			return 'No min value for empty list'

	def size(self):
		return len(self.content)

	def isEmpty(self):
		return not bool(self.content)

	def peek(self):
		if self.content:
			return self.content[-1]
		else:
			print('Stack is empty')

	def __repr__(self):
		return '{}'.format(self.content)


def Compile_Stack_v1():
	q = Stack()
	for i in range(15, 20):
		q.push(i)
	for i in range(10, 5, -1):
		q.push(i)
	for i in range(1, 13):
		print(q.pop(), q.find_min())

Compile_Stack_v1()
# Another approach to implement a stack is by thinking of it as a container of nodes(objects) following a LIFO order:

class Node(object):
	def __init__(self, value= None, pointer=None):
		self.value = value
		self.pointer = pointer
class Stack2(object):
	def __init__(self):
		self.head = None
	def isEmpty(self):
		return not bool(self.head)
	def push(self, item):
		self.head = Node(item, self.head)
	def pop(self):
		if self.head: # if it is not false
			node = self.head
			self.head = node.pointer
			return node.value
		else:
			print('Stack is empty')
	def peek(self):
		if self.head:
			return self.head.value
		else:
			print('Stack is empty')
	def size(self):
		node = self.head
		count = 0
		while node:
			count += 1
			node = node.pointer
		return count
	def _printList(self):
		node = self.head
		while node:
			print(node.value)
			node = node.pointer

def Compile_Stack_v2():
	stack = Stack2()
	print('Is the stack empty: ', stack.isEmpty())
	print('Adding 1 to 10 in the stack...')
	for i in range(1, 11):
		stack.push(i)
	stack._printList()
	print('Stack size: ', stack.size())
	print('Stack peek: ', stack.peek())
	print('Popping...', stack.pop())
	print('Stack peek after pop: ', stack.peek())
	print('Is the stack empty now?' , stack.isEmpty())

Compile_Stack_v2()


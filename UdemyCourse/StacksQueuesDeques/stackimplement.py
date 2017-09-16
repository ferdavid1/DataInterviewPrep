'''
Stack() creates a new Empty stack - it needs no paramters and returns an empty stack
push(item) adds a new item to the top of the stack. It needs the item and returns nothing.
pop() removes the top item from the stack
isEmpty() tests whether the stack is empty. it needs no parameters and returns a boolean value
size() returns the number of items on a stack. no parameters, returns an int
'''
class Stack():
	def __init__(self):
		self.curr = []
	def push(self, x):
		curr = self.curr
		curr.append(x)
	def pop(self):
		curr = self.curr
		if curr:
			curr.pop()
		else: 
			print("Stack is empty, can't pop!")
	def isEmpty(self):
		curr = self.curr
		# if not curr:
		# 	return True
		# return False
		return curr == []
	def size(self):
		curr = self.curr
		return len(curr)
	def peek(self):
		curr = self.curr
		return curr[-1]

if __name__ == '__main__':
	s = Stack()
	for x in range(10):
		s.push(x)
	s.pop()
	print(s.curr, s.isEmpty(), s.size(), s.peek())


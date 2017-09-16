'''
Given the Stack Class, implement a Queue class using two stacks
Use a python list data structure as each of the stacks
'''
class Queue2Stacks():
	
	def __init__(self):
		self.stack1 = []
		self.stack2 = []

	def enqueue(self, x):
		instack = self.stack1
		instack.append(x)

	def dequeue(self):
		instack = self.stack1
		outstack = self.stack2
		if not outstack: # if oustack is empty
			while instack: # while instack has values
				val = instack.pop()
				outstack.append(val)
		return outstack.pop()

if __name__ == '__main__':
	"""
	RUN THIS CELL TO CHECK THAT YOUR SOLUTION OUTPUT MAKES SENSE AND BEHAVES AS A QUEUE
	"""
	q = Queue2Stacks()

	for i in range(5):
	    q.enqueue(i)
	print(q.stack1)
	for i in range(5):
	    q.dequeue()
	print(q.stack2)
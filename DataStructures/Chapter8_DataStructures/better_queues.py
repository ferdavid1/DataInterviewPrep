# a better way to write queues, using two stacks (two lists) instead of one

class Queue(object):

	def __init__(self):
		self.in_stack = []
		self.out_stack = []

	def _transfer(self):
		while self.in_stack:
			self.out_stack.append(self.in_stack.pop()) # add the last element of the in stack the the out_stack

	def enqueue(self, item):
		return self.in_stack.append(item)

	def dequeue(self):
		if not self.out_stack:
			self._transfer() # if out stack is empty, transfer from the last element of in stack

		if self.out_stack:
			return self.out_stack.pop() # if out stack is not empty, remove the last element

		else:
			return 'Queue Empty!'

	def size(self):
		return len(self.in_stack) + len(self.out_stack)

	def peek(self):
		if not self.out_stack:
			self._transfer()
		if self.out_stack:
			return self.out_stack[-1]
		else:
			return 'Queue empty!'

	def __repr__(self):
		if not self.out_stack:
			self._transfer()
		if self.out_stack:
			return '{}'.format(self.out_stack)
		else:
			return 'Queue empty'

	def isEmpty(self):
		return not (bool(self.in_stack) or bool(self.out_stack))

if __name__ == '__main__':
	queue = Queue()
	print("Is the queue empty? ", queue.isEmpty())
	print("Adding 0 to 10 in the queue...")
	for i in range(10):
		queue.enqueue(i)
	print("Queue size: ", queue.size())
	print("Queue peek : ", queue.peek())
	print("Dequeue...", queue.dequeue())
	print("Queue peek: ", queue.peek())
	print("Is the queue empty? ", queue.isEmpty())
	print("Printing the queue...")
	print(queue)
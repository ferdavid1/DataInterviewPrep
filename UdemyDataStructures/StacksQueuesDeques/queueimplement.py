'''
Queue() creates a new queue (empty)
enqueue() adds a new item to the rear of the queue, takes in item returns nothing
dequeue() removes the front item from the queue
isEmpty()
size()
peek()
'''
class Queue():

	def __init__(self):
		self.items = []

	def enqueue(self, x):
		items = self.items
		items.insert(0, x)

	def dequeue(self):
		items = self.items
		if items:
			items.pop()
		else:
			print("Nothing to pop!")

	def isEmpty(self):
		items = self.items
		return items == []

	def size(self):
		items = self.items
		return len(items)

	def peek(self):
		items = self.items
		print(items)
		return items[-1]

if __name__ == '__main__':
	q = Queue()
	for x in range(5):
		q.enqueue(x)
	for x in range(3):
		q.dequeue()
	print(q.items, q.isEmpty(), q.size(), q.peek())

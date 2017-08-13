'''
A Queue, as opposed to a stack, is a structure where the first enqueued element (at the back) will be the first one to be 
dequeued (when it is at the front), being defined as a first-in-first-out (FIFO) structure. You can think of a queue as a 
line of people waiting for a roller coaster ride.

Array access of elements in queues is restricted and queues should have the following operations running at O(1):
	
	Enqueue: Insert an item at the back of the queue
	Dequeue: Removce an item from the front of queue
	Peek/front: Retrieve an time at the front of the queue without removing it
	Empty/size: Check whether the queue is empty or give its size

Again, we can write a queue class with lists, but it'll be inefficient, because it uses insert(), which is slow
'''
class Queue(object):

		def __init__(self):
			self.items = []

		def isEmpty(self):
			return not bool(self.items)

		def enqueue(self, item):
			self.items.insert(0, item) # the 'back' of the queue is the first element, with index 0

		def dequeue(self):
			# self.items.insert(-1, item) one option
			return self.items.pop() # better option

		def size(self):
			return len(self.items)

		def peek(self):
			return self.items[-1]

		def __repr__(self):
			return '{}'.format(self.items)

if __name__ == '__main__':
	queue = Queue()
	print('Is the queue empty? ', queue.isEmpty())
	print("Adding 0 to 10 in the queue...")
	for i in range(10):
		queue.enqueue(i)
	print("Queue size: ", queue.size())
	print("Queue peek : ", queue.peek())
	print("Dequeue...", queue.dequeue())
	print("Queue peek: ", queue.peek())
	print("Is the queue empty? ", queue.isEmpty())
	print(queue)


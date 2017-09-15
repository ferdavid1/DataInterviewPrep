'''
Deque() creates an empty Deque.
addFront(item) adds an item to the front of the Deque
addRear(item) adds an item to its back
removeFront(item)
removeRear(item)
isEmpty()
size()
peek()
'''
class Deque():

	def __init__(self):
		self.items = []

	def addFront(self, x):
		items = self.items
		items.append(x)
	
	def removeFront(self):
		items = self.items
		if items:
			items.pop()
		else:
			print("Nothing to remove!")

	def addRear(self, x):
		items = self.items
		items.insert(0, x)

	def removeRear(self):
		items = self.items
		if items:
			items.pop(0)
		else:
			print("Nothing to remove!")	

	def isEmpty(self):
		items = self.items
		return items == []

	def size(self):
		items = self.items
		return len(items)

if __name__ == '__main__':
	d = Deque()
	for x in range(5):
		d.addFront(x)
	for x in range(3):
		d.removeFront()
	print(d.items)
	print(d.size(), d.isEmpty())
	d2 = Deque()
	for x in range(5):
		d2.addRear(x)
	for x in range(3):
		d2.removeRear()
	print(d2.items)
	print(d2.size(), d2.isEmpty())

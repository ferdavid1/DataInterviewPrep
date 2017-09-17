
class DoublyLinkedListNode(object):

	def __init__(self, value):
		self.value = value
		self.nextnode = None
		self.prevnode = None

if __name__ == '__main__':
	a = DoublyLinkedListNode(1)
	b = DoublyLinkedListNode(2)
	c = DoublyLinkedListNode(3)

	a.nextnode = b
	a.prevnode = None
	b.nextnode = c
	b.prevnode = a
	c.nextnode = None
	c.prevnode = b
	print(b.nextnode.value, c.prevnode.value)

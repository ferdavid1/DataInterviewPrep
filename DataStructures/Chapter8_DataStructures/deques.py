'''
A deque is a double-ended queue, which can roughly be seen as a union of a stack and a queue.
Python has an efficient deque implementation with fast appending and popping from both ends
'''

from collections import deque
q = deque(['buffy', 'xander', 'willow'])
print(q)
q.append('giles')
print(q)
q.popleft()
q.pop()
print(q)
q.appendleft('angel')
print(q)

'''
Interestingly, deques in Python are based on a doubly linked list, not in dynamic arrays. 
It means that operations such as inserting an item anywhere are fast - O(1) - but arbitrary index accessing are slow - O(n).
'''

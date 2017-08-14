'''
Conceptually, a heap is a binary tree where each node is greater in value than its children
We will learn about trees in the next chapters but we should aready keep in mind that when modifications are made 
in a balanced tree, we can repair its structure with O(logn) runtime.

Heaps are generally useful for applications that repeatedly acccess the greatest element in the list.
A min/max heap lets you to find the smallest/largest element in O(1) and to extract/add/replace it in O(ln n)

Python's heapq package provides functions to insert and remove items while keeping the sequence as a heap.

We can use the heapq.heapify(x) method to transform a list into a heap, in-place, and in O(n) time. 
'''
import heapq

l = [4,6,8,1]
heapq.heapify(l)
print(l)

h = []
heapq.heappush(h, (1, 'food'))
heapq.heappush(h, (2, 'have fun'))
heapq.heappush(h, (3, 'work'))
heapq.heappush(h, (4, 'study'))
print(h)

heapq.heappop(l)
print(l)

'''
The method heapq.heappushpop(heap, item) is used to push the item on the heap, 
then it pops and returns the smallest item from the heap.

In a similar way, heapq.heapreplace(heap, item) will pop and return the smallest item from the heap, then push
the new item. In case the heap size does not change

Several other operations are available with a heap proprietes.
For example heapq.merge(*iterables) will merge multiple sorted inputs into a single sorted output (returning an iterator):
'''
for x in heapq.merge([1,3,5], [2,4,6]):
	print(x, end='\n')

'''THIS IS SO COOL!!!!'''

'''
Finally, the methods heapq.nlargest(n, iterable[, key]) and heapq.nsmallest(n, iterable[, key])
will return a list with the n largest and smallest elements from the dataset defined by iterable

'''
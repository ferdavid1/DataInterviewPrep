# Don't need to specify how large an array is beforehand
'''
A list instance often has greater capacity than current length.
If elements keep getting appended, eventually this extra
space runs out.
'''

import sys

# Set n
n = 50

data = []

for i in range(n):
	# Number of elements
	a = len(data)
	# Actual size in Bytes
	b = sys.getsizeof(data)

	print("Length: {}, Size in bytes: {}".format(a,b))

	data.append(n)

# THIS IS SO LIT!

# its size in chunks available is increased.

# Dynamic array implementation
'''
1. Allocate a new array B with larger capacity
2. Set B[i] = A[i] for i=0, ..., n-1 where n denotes current number of items
3. Set A=B, that is, we henceforth use B as the array support the list
4. Insert the new element in the new array.
'''

'''
a.) create a new array B
b.) store elements of A in B
c.) reassign reference A to the new array
'''

'''
Problems:
	How large of an array to create?
	A commonly used rule is for the new array to 
	have twice the capacity of the existing array that 
	has been filled.
	We'll see the mathematic reasoning behind this later
'''

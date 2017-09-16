# 'array sequence' is the general term
# Python has 3 main sequence classes:
	# list: [1,2,3]
	# tuple: (1,2,3)
	# string: '123'
# all support indexing (e.g. t[0]=1)

'''
How computers store information
	Focus on computer memory
	Units of memory (bits and bytes)
	Memory retrieval 
'''

'''
Memory of a computer is stored in bits
typical unit of byte, which is 8 bits
Computers typicallu use a memory address 
Each byte is associated with unique address.
	Byte #2144 vs Byte #2147
'''

'''
Computer hardware is designed, in theory, so that
any byte of the main memory can be efficiently accessed
Computer's main memory performs as random access memory (RAM)
Just as easy to retrieve byte #8675309 as it is to retrieve byte #309
Individual byte of memory can be stored or retrieved in O(1) time
'''

'''
Programming language keeps track of the association between an 
identifier and the memory address.
May want a video game to keep track of the top ten scores for
that game. 
Prefer to use a single name for the group
Use index number to refer to the high scores in that group
'''

''' 
A group of related variables can be stored one after another 
in a contiguous portion of the computer's memory
We will denote such a representation as an array
A text string is stored as an ordered sequence of individual characters.
Python internally represents each Unicode character with 16 bits (i.e. 2 bytes)
'''

'''
Six-character string, such as "SAMPLE" would be stored in 12 consecutive bytes of memory
This is an array of six characters.
Each location within an array as a cell
Integer index to describe its location
'''

'''
Each cell of an array uses the same number of bytes
Allows any cell to be accessed in constant time
Appropriate memory address can be computed using the 
calculation, start + (cellsize)(index)
'''

'''
Arrays have higher level abstraction

# Referential Arrays:
	Imagine 100 student names with ID numbers
	Each cell of the array needs to have the same number of bytes
	How can we avoid having to have a series of names
	We can use an array of object References
'''

'''
Each element is a reference to the object
'Joseph' -> element 1 in the array
'Rene' -> element 2 in the array
'Janet' -> element 3 in the array
'Jonas' -> element 4 in the array
'Helen' -> element 5 in the array
'Virginia' -> element 6 in the array
'''

'''
A single list instance may include multiple references to 
the same object as elements of the list
Single object can be an element of two or more lists
When computing the slice of a list, the result is a 
new list instance.
New list has references to the same elements that are in 
in the original list.
'''

# Copying Arrays
'''
backup = list(previouslist)
This produces a new list that is a shallow copy
in that it references the same elements as in the first list
If the contents of the list were of the mutable type, a deep
copy, meaning a new list with new elements, can be produced
by using the deepcopy function from the copy module
'''

'''
Counters = [0]*8
all eight cells reference the same object
Counters[2] += 1
Does not technically change the value of the existing integer instance.
This computes a new integer
'''

'''
list.extend(extra_items)
'''

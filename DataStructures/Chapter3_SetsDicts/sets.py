# a set is an unordered collection data type that is iterable, mutable, and has no duplicate elements. 
# Sets are used for membership testing and eliminating duplicate entries
# Since sets have O(1) insertion, the runtime of 'union' is O(m+n)
# for 'intersection', it is only necessary to transverse the smaller set, so the runtime is O(n).

# Frozen sets are immutable objects that only support methods and operators that produce a rusult without affecting set to which they are applied

# the add(x) method:
people = {'Buffy', "Angel", "Giles"}
people.add("Willow")
print(people)

# the s.update(t) or s| =t methods:
	# both return a set s with elements added from t

# the s.union(t) or s|t methods:
	#perform union of the two sets

# the s.difference(t) or s - t methods:
	# return a new set that has every item that is not in the second set
people = {'Buffy', "Angel", "Giles", "Xander"}
vampires = {"Spike", "Angel", "Drusilia"}
print(people.difference(vampires))

# the clear() method:
people = {'Buffy', "Angel", "Giles"}
people.clear()
print(people)

# the discard(x), remove(x), and pop() methods;
	# discard(x) removes the item from the set or raises KeyError if not in set
	# pop() returns and removes a random item from the set or raises a KeyError if not in set

#Sets with lists and dictionaries
	# you can cast a set from a list
def difference(l1):
	'''return the list with duplicate elements removed'''
	return list(set(l1))
def intersection(l1, l2):
	'''return the intersection of two lists'''
	return list(set(l1) & set(l2))
def union(l1, l2):
	'''return the union of two lists'''
	return list(set(l1) | set(l2))
def test_sets_operations_with_lists():
	l1 = [1,2,3,4,5,9,11,15]
	l2 = [4,5,6,7,8]
	l3 = []
	assert(difference(l1) == [1,2,3,4,5,9,11,15])
	assert(difference(l2) == [8,4,5,6,7])
	assert(intersection(l1,l2) == [4,5])
	assert(union(l1, l2) == [1,2,3,4,5,6,7,8,9,11,15])
	assert(difference(l3) == [])
	assert(intersection(l3,l2) == l3)
	assert(sorted(union(l3, l2)) == sorted(l2))
	print('Tests passed!')

# we can also use set properties in dicts
from collections import OrderedDict

def set_operations_with_dict():
	pairs =  [('a',1), ('b',2), ('c',3)]
	d1 = OrderedDict(pairs)
	print(d1)

	d2 = {'a':1, 'c':2, 'd':3, 'e':4}
	print(d2)

	union = d1.keys() & d2.keys()
	print(union)

	union_items = d1.items() & d2.items() #values of each key
	print(union_items)

	subtraction1 = d1.keys() - d2.keys()
	print(subtraction1)

	subtraction2 = d2.keys() - d1.keys()
	print(subtraction2)

	subtraction_items = d1.items() - d2.items()
	print(subtraction_items)

	d3 = {key:d2[key] for key in d2.keys() - {'c', 'd'}}
	# print(d3) {'a':1, 'e':4}



if __name__ == '__main__':
	test_sets_operations_with_lists()
	set_operations_with_dict()
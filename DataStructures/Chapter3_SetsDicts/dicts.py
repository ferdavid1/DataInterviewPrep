# dictionaries (in python) are implemented using hash tables
# hashing functions assign integer values to an arbitrary object in constant time, which can be used as an index into an array
print(hash(42))
print(hash('hello'))

# a dict is a collection mapping type that is iterable and supports the membership operator in and the size function len()
# when iterated, unordered mapping types provide their items in an arbitrary order
# accessing dictionaries has runtime O(1) so they are used to keep counts of unique items
	# for example, counting the number of each unique word in a file
	# they are also used for fast membership test

tarantino = {}
tarantino['name'] = 'Quentin Tarantino'
tarantino['job'] = 'director'
print(tarantino)

# a hash table is a data structure used to implement an associative array, a structure that can map keys to values

sunnydale = dict({'name':'Buffy', 'age':16, 'hobby':'slaying'})
print(sunnydale)
sunnydale = dict(name='Giles', age = 45, hobby='Watch')
print(sunnydale)

# the pop() and popitem() methods:
	# the pop() method removes an arbitrary item from the dictionary, returning it. 
	# the popitem() method removed an arbitrary (key, value) tuple from the dictionary, also returning it

# the clear() method: removes all items in the dictionary
sunnydale.clear()
print(sunnydale)

#runtime analysis for dictionaries
import timeit
import random

# for i in range(10000, 1000001, 20000):
# 	t = timeit.Timer("random.randrange(%d) in x" %i, "from __main__ import random,x")
# 	x = list(range(i))
# 	lst_time = t.timeit(number=1000)
# 	x = {j:None for j in range(i)}
# 	d_time = t.timeit(number=1000)
# 	print("%d, %10.3f, %10.3f" % (i, lst_time, d_time))

# we find out from the output that lists have O(n) and dicts have O(1)

# iterating over dictionaries
	# a loop over a dictionary iterates over its keys by default
	# the keys will appear in an arbitrary order but we can use sorted() to iterate over the items in a sorted way
	# this also works for the attributes keys(), values(), and items()
# for key in sorted(dict.keys()):
# 	print(key, dict[key])

def items_in_key_order(d):
	for key in sorted(d):
		yield key, d[key]

# Python's collection data types
	# python's collections module implements specialized container data types providing high-performance alternative to the general purpose built-in containers
from collections import defaultdict

def defaultdict_example():
	pairs = {('a',1), ('b',2), ('c', 3)}
	d1 = {}
	for key, value in pairs:
		if key not in d1:
			d1[key] = []
		d1[key].append(value)
	print(d1)

	d2 = defaultdict(list)
	for key, value in pairs:
		d2[key].append(value)
	print(d2)

# Ordered Dictionaries
	# ordered dictionaries are an ordered mapping type provided by Python's collections.OrderedDict.
	# They have all the methods and properties of a built-in dict, but in addition they store items in the insertion order

from collections import OrderedDict

# 	pairs = [('a',1), ('b',2), ('c',3)]
# 	d1 = {}
# 	for key, value in pairs:
# 		if key not in d1:
# 			d1[key] = []
# 			d1[key].append(value)
# 	for key in d1:
# 		print(key, d1[key])

# 	d2 = OrderedDict(pairs)
# 	for key in d2:
# 		print(key, d2[key])

tasks = OrderedDict()
tasks[8031] = 'Backup'
tasks[4027] = 'Scan Email'
tasks[5733] = 'Build System'

print(tasks)

from collections import Counter

def Counter_example():
	seq1 = [1,2,3,5,1,2,5,5,2,5,1,4]
	seq_counts = Counter(seq1)
	print(seq_counts)

	seq2 = [1,2,3]
	seq_counts.update(seq2)
	print(seq_counts)

	seq3 = [1,4,3]
	for key in seq3:
		seq_counts[key] += 1
	print(seq_counts)

	seq_counts_2 = Counter(seq3)
	print(seq_counts_2)
	print(seq_counts + seq_counts_2)
	print(seq_counts - seq_counts_2)
	return 'done'

# print(Counter_example())

# Counting frequency of items in a sequence
def find_top_N_recurring_words(seq,N):
	dcounter = Counter()
	for word in seq.split():
		dcounter[word] += 1
	return dcounter.most_common(N)

import string 
import sys
import collections

def count_unique_word():
	words = collections.defaultdict(int)
	strip = string.whitespace + string.punctuation + string.digits + "\"'"
	for filename in sys.argv[1:]:
		with open(filename) as file:
			for line in file:
				for word in line.lower().split():
					word = word.strip(strip)
					if len(word) > 2:
						words[word] = +1
	for word in sorted(words):
		print("'{0}' occurs {1} times.".format(word, words[word]))
	return 'done'

count_unique_word()

# Anagrams 
	# sets do not count occurence, and sorting a list is O(nlogn), hash tables can be a good solution for this tpe of problem
def is_anagram(s1,s2):
	counter = Counter()
	for c in s1:
		counter[c] += 1
	for c in s2:
		counter[c] -= 1
	for i in counter.values():
		if i:
			return False
	return True

# Sums of Paths
# this program uses two different dictionary containers to determine the number of ways two die can sum to a certain value

def find_dice_probabilities(S, n_faces=6):
	if S > 2*n_faces or S <2:
		return None
	cdict = Counter()
	ddict = defaultdict()

	for dice1 in range(1, n_faces+1):
		for dice2 in range(1, n_faces+1):
			t = [dice1, dice2]
			cdict[dice1 + dice2] += 1
			ddict[dice1 + dice2].append(t)
	return [cdict[S], ddict[S]]

print(is_anagram('wakafloca', 'acolfakwa'))
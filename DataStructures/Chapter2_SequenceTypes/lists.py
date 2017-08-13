q = [2,3]
p = [1,q,4]
p[1].append("buffy")
print(p)
print(q)
# insertions or removals at the end make for the quickest runtime - O(1)
# remove() or index() makes things slower - O(n)
# append(x) does the same as list[len(list):] = x
people = ["Buffy", "Faith"]
people.append("Giles")
print(people)
people[len(people):] = ["Xander"]
print(people)

#extend(c) adds all the individual letters of s
people = ["Buffy", "Faith"]
people.extend("Giles")
print(people)
people += "Willow" #this des the same
print(people)
people += ["Xander"] # this appends with a different but equal method
print(people)

#insert(i, x) inserts x in [1] of the list
people = ["Buffy", "Faith"]
people.insert(1, "Xander")
haha = "wow"
print(haha)

print(haha.replace("wow","wowthanks")) #reminder of replace method

#remove() -akin to strip('chars') for strings
people.remove("Buffy")
print(people)

#pop() method - removes, returns the item at given position. If no position given, returns the LAST item
people = ["Buffy", "Faith"]
print(people.pop())
print(people)

# del function removes an object from a list given its index, not its value like remove()
a = [-1,4,5,7,10]
del a[0]
print(a)
del a[2:3]
print(a)

#index()
people = ["Buffy", "Faith"]
print(people.index("Buffy"))

#count(x)
print(people.count("Buffy"))

#sort() sorts alphabetically or by numerical order
people = ["Xander", "Faith", "Buffy"]
people.sort()
print(people)

#reverse() sorts in reverse
people.reverse()
print(people)

#list unpacking
# similar to unpacking in tuples
first, *rest = [1,2,3,4,5]
print(first)
print(rest)

#starred arguments
def example_args(a,b,c):
	return a * b * c

L = [2,3,4]
print(example_args(*L)) # whoa this is hella cool

print(example_args(2, *L[1:])) # same thing being said a different way

# List Comprehensions
a = [y for y in range(1900, 1940) if y%4 == 0]
print(a)

b = [2**i for i in range(13)]
print(b)

c = [x for x in a if x%2==0]
print('c: {}'.format(c))

d = [str(round(355/113.0,i)) for i in range(1,6)]
print(d)

words = 'Buffy is awesome and a vampire slayer'.split()
e = [[w.upper(), w.lower(), len(w)] for w in words]
print([i for i in e])

# if you have to use two for or if statements, dont use list comprehension. 
	# Using it would eliminate the advantage in speed of using list comprehension versus a proper loop

# Good example:
result = []
for x in range(10):
	for y in range(5):
		if x * y > 10:
			result.append((x,y))

for x in range(5):
	for y in range(5):
		if x != y:
			for z in range(5):
				if y != z:
					# print(x,y,z)
					pass
squares = [x for x in range(10)]
# eat(jelly_bean for jelly_bean in jelly_beans if jelly_bean.color == 'black')

# Bad Example:
result = [(x,y) for x in range(10) for y in range(5) if x*y > 10]

# Runtime Analysis for Lists
def test1():
	l = []
	for i in range(1000):
		l = l + [i] # same thing as l.append(i)
def test2():
	l = []
	for i in range(1000):
		l.append(i)
def test3():
	l = [ i for i in range(1000)] # same thing as l.append(i) after for loop
def test4():
	l = list(range(1000))

if __name__ == '__main__':
	import timeit
	t1 = timeit.Timer("test1()", "from __main__ import test1")
	print('concat ',t1.timeit(number=1000), "milliseconds")
	t2 = timeit.Timer("test2()", "from __main__ import test2")
	print('append ',t2.timeit(number=1000), "milliseconds")
	t3 = timeit.Timer("test3()", "from __main__ import test3")
	print("comprehension ",t3.timeit(number=1000), "milliseconds")
	t4 = timeit.Timer("test4()", "from __main__ import test4")
	print("list range ",t4.timeit(number=1000), "milliseconds")


	''' Output:
	concat  4.619928618220829 milliseconds
	append  0.18369518070353585 milliseconds
	comprehension  0.08212117588049139 milliseconds
	list range  0.033658231395487626 milliseconds
	'''
'''
Operation Big-O Efficiency
index [] 	O(1)
index assignment O(1)
append 		O(1)
pop() 		O(1)
pop(i) 		O(n)
insert(i,item) 	O(n)
del operator 	O(n)
iteration 		O(n)
contains (in) 	O(n)
get slice [x:y] O(k)
del slice 		O(n)
set slice 		O(n+k)
reverse 		O(n)
concatenate 	O(k)
sort 			O(n log n)
multiply 		O(nk)
'''


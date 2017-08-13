# range()

# enumerate()
	# make grep from enumerate
import sys

def grep_word_from_files():
	word = sys.argv[1]
	for filename in sys.argv[2:]:
		with open(filename) as file:
			for line_index, line in enumerate(file, start=1):
				if word in line:
					print("{0}:{1}:{2:.40}".format(filename, line_index, line.rstrip()))

# if __name__ == '__main__':
# 	if len(sys.argv) < 2:
# 		print("Usage: grep_word_from_files.py word infile1 [infile2...]")
# 	else:
# 		grep_word_from_files()

# zip()
a = [1,2,3,4,5]
b = ['a','b','c','d','e']
together = list(zip(a,b))
print(together)

# filter(function, sequence) --- super useful --- 
	# returns a sequence consisting of items for which function(item) is true
def f(x): return x % 2 !=0 and x % 3 != 0
print(f(33))
print(f(17))
myfilter = filter(f, range(2, 25))
print(list(myfilter))

# map(function, list)
	# applies a function to every item of an iterable (read: list) and then returns a list of the results
def cube(x): return x**3
mymap = map(cube, range(1,11))
print(list(mymap))

# the lambda function
	# a dynamic way of compacting functions inside the code
# for example, the function:
def area(b, h):
	return 0.5 * b * h #area of a triangle
print(area(5,4))
# could be rewritten as:
area = lambda b, h: 0.5 * b* h
print(area(5,4))


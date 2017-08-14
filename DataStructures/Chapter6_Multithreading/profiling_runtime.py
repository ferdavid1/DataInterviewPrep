# finding performance bottlenecks and optimizing code

# prefer tuples to lists with read-only data

# use generators rather than large lists or tuples to iteration
# Ex:
# instead of:
mylist = [x for x in range(14)]
# use a generator, replacing [] with ()
mygenerator = list(x for x in range(14))
import timeit
print('List time: {}'.format(timeit.timeit(str(mylist))))
print('Generator time: {}'.format(timeit.timeit(str(mygenerator))))
# List time: 0.22544591259800706
# Generator time: 0.19270341066798757

# when creating large strings out of small strings, instead of concatenating the small, accumulate them all in a list and 'join' the list of strings in the end
# Ex:
a = 'a'; b = 'b'; c = 'c'
# instead of: 
concat = a + b + c
# use:
joined = ''.join([a,b,c])

# the cProfile package
# this package providesa detailed breakdown of call times and can be used to find performance bottlenecks
import cProfile
cProfile.run('some_function()')


'''
Fibonacci Sequence: Recursively, Dynamically(Memoization),
Iteratively)
'''
def fib_rec(n):
	if n ==0 or n == 1:
		return n
	return fib_rec(n-1) + fib_rec(n-2)

def fib_iter(n):
	if n==0 or n==1:
		return n
	lst = [0,1]
	for x in range(2,n+1):
		lst.append(lst[x-1] + lst[x-2])
	return lst[-1]

def fib_dyn(n):
	if n==0 or n==1:
		return n
	d = {0:0, 1:1}
	for x in range(2, n+1):
		d[x] = d[x-1] + d[x-2]
	return d[n]
"""
UNCOMMENT THE CODE AT THE BOTTOM OF THIS CELL TO SELECT WHICH SOLUTIONS TO TEST.
THEN RUN THE CELL.
"""

from nose.tools import assert_equal

class TestFib(object):
    
    def test(self,solution):
        assert_equal(solution(10),55)
        assert_equal(solution(1),1)
        assert_equal(solution(23),28657)
        print ('Passed all tests.')
# UNCOMMENT FOR CORRESPONDING FUNCTION
t = TestFib()

# t.test(fib_rec)
t.test(fib_dyn) # Note, will need to reset cache size for each test!
# t.test(fib_iter)
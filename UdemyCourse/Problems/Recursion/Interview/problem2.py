'''
String Permutation

Given a string, write a function that uses recursion to output a list of all the possible permutations of that string
Ex: 'abc' = ['abc',  'acb', 'bac', 'bca', 'cab', 'cba']

Note: treat each string character as distinct
'''
def factorial(i):
	if i < 2:
		return 1
	return i * factorial(i-1)
def permute(s):

	lst = []
	perms = factorial(len(s))




"""
RUN THIS CELL TO TEST YOUR SOLUTION.
"""

from nose.tools import assert_equal

class TestPerm(object):
    
    def test(self,solution):
        
        assert_equal(sorted(solution('abc')),sorted(['abc', 'acb', 'bac', 'bca', 'cab', 'cba']))
        assert_equal(sorted(solution('dog')),sorted(['dog', 'dgo', 'odg', 'ogd', 'gdo', 'god']) )
        
        print ('All test cases passed.')
        


# Run Tests
t = TestPerm()
t.test(permute)

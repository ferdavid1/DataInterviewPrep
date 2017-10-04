
def permute(s):
	output = []
	if len(s) ==1: #list initiation would get overwritten by recursion
		output = [s]
	else:
		for ind, x in enumerate(s):
			for perm in permute(s[:ind] + s[ind+1:]):
				output += [x + perm]
	return output
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
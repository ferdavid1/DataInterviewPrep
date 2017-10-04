'''
Reverse a string recursively (remember to think in terms of the base case)
No python tricks ([::-1] or iteration)
'''
def reverse(s):

	if s == '':
		return '' 
	
	last = s[-1]
	s = s[:-1]
	return last + reverse(s)

if __name__ == '__main__':
	'''
	RUN THIS CELL TO TEST YOUR FUNCTION AGAINST SOME TEST CASES
	'''

	from nose.tools import assert_equal

	class TestReverse(object):
	    
	    def test_rev(self,solution):
	        assert_equal(solution('hello'),'olleh')
	        assert_equal(solution('hello world'),'dlrow olleh')
	        assert_equal(solution('123456789'),'987654321')
	        
	        print 'PASSED ALL TEST CASES!'
	        
	# Run Tests
	test = TestReverse()
	test.test_rev(reverse)
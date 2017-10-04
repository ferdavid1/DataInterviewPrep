def finder(arr1,arr2):
    
    for x in arr1:
    	if arr2.count(x) != arr1.count(x):
    		return x
    return


"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

class TestFinder(object):
    
    def test(self,sol):
        assert_equal(sol([5,5,7,7],[5,7,7]),5)
        assert_equal(sol([1,2,3,4,5,6,7],[3,7,2,1,4,6]),5)
        assert_equal(sol([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1]),6)
        print ('ALL TEST CASES PASSED')

# Run test
t = TestFinder()
t.test(finder)
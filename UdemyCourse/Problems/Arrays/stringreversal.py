'''
"Cheating way":
list = list[::-1]
'''

"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
def rev_word(s):
	print(s.split()[::-1])
	return " ".join(s.split()[::-1])

from nose.tools import assert_equal

class ReversalTest(object):
    
    def test(self,sol):
        assert_equal(sol('    space before'),'before space')
        assert_equal(sol('space after     '),'after space')
        assert_equal(sol('   Hello John    how are you   '),'you are how John Hello')
        assert_equal(sol('1'),'1')
        print ("ALL TEST CASES PASSED")
        
# Run and test
t = ReversalTest()
t.test(rev_word)
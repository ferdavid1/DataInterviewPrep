'''
"Cheating way":
list = list[::-1]
'''

"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
def rev_word(s):
	s = s.strip().replace("    ", ",").replace(",", " ")
	words = []
	for ind, x in enumerate(s[:-2]):
		if not x.isalpha():
			if s[ind+1].isalpha():
				words.append(s[:ind+1:])
				words.append(s[ind+1:])
			else:
				pass
	print(words)


from nose.tools import assert_equal

class ReversalTest(object):
    
    def test(self,sol):
        # assert_equal(sol('    space before'),'before space')
        # assert_equal(sol('space after     '),'after space')
        assert_equal(sol('   Hello John    how are you   '),'you are how John Hello')
        assert_equal(sol('1'),'1')
        print ("ALL TEST CASES PASSED")
        
# Run and test
t = ReversalTest()
t.test(rev_word)
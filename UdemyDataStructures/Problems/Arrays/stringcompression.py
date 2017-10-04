from collections import OrderedDict
def compress(s):
    uniq = OrderedDict()
    for x in s:
    	uniq[x] = True
    result = ""
    for el in uniq:
    	result += str(el + str(s.count(el)))
    return result

# compress('AAAAABBBBCCCC') -> 'A5B4C4'
"""
RUN THIS CELL TO TEST YORU SOLUTION
"""
from nose.tools import assert_equal

class TestCompress(object):

    def test(self, sol):
        assert_equal(sol(''), '')
        assert_equal(sol('AABBCC'), 'A2B2C2')
        assert_equal(sol('AAABCCDDDDD'), 'A3B1C2D5')
        print 'ALL TEST CASES PASSED'

# Run Tests
t = TestCompress()
t.test(compress)
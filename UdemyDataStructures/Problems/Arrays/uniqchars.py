from collections import OrderedDict
def uni_char(s):
    d = OrderedDict()
    for x in s:
    	d[x] = True
    if "".join(d.keys()) == s:
    	return True
    return False

"""
RUN THIS CELL TO TEST YOUR CODE>
"""
from nose.tools import assert_equal


class TestUnique(object):

    def test(self, sol):
        assert_equal(sol(''), True)
        assert_equal(sol('goo'), False)
        assert_equal(sol('abcdefg'), True)
        print 'ALL TEST CASES PASSED'
        
# Run Tests
t = TestUnique()
t.test(uni_char)
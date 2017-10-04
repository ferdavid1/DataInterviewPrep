'''
Given two strings, check whether they are anagrams
Ignore spaces and capitalization
'''

def anagram(s1, s2):
    s1_counts = {}
    s2_counts = {}
    s1, s2 = s1.replace(" ", "").lower(), s2.replace(" ", "").lower()
    for i in s1:
        s1_counts[i] = s1.count(i)
    for j in s2:    
        s2_counts[j] = s2.count(j)
    if s1_counts == s2_counts:
        return True 
    return False

"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

class AnagramTest(object):
    
        def test(self,sol):
                assert_equal(sol('go go go','gggooo'),True)
                assert_equal(sol('abc','cba'),True)
                assert_equal(sol('hi man','hi     man'),True)
                assert_equal(sol('aabbcc','aabbc'),False)
                assert_equal(sol('123','1 2'),False)
                print ("ALL TEST CASES PASSED")

# Run Tests
t = AnagramTest()
t.test(anagram)

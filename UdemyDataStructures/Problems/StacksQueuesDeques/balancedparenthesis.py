'''
Given a string of opening and closing parentheses, check whether its balanced. 
3 types: (), [], {}
Assume that the string doesn't contain any other character
than these, no spaces, words, or numbers. 
As a reminder, balanced parentheses require every opening parenthesis 
to be closed in the reverse order opened. 
Assume the input string has no spaces
'''
import timeit
def balance_check_nostack(s): # without stack
    left1 = s.count('(')
    right1 = s.count(')')
    left2 = s.count('[')
    right2 = s.count(']')
    left3 = s.count('{')
    right3 = s.count('}')
    return left1 == right1 and left2 == right2 and left3 == right3

class Stack():

	def __init__(self):
		self.items = []

	def push(self, x):
		items = self.items
		items.append(x)

	def pop(self):
		items = self.items
		if items:
			items.pop()
		else:
			"Nothing to pop!"

	def isEmpty(self):
		items = self.items
		return items == []

	def size(self):
		items = self.items
		return len(items)

	def peek(self):
		items = self.items
		return items[-1]

def balance_check(s): # with stack
	opened = ['(', '{', '[']
	closed = [')', '}', ']']
	stack = Stack()
	for item in s:
		if item in opened: 
			stack.push(item)
		elif item in closed:
			if stack.isEmpty():
				return False
			else:
				stack.pop()
	if stack.isEmpty():
		return True
	return False

"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

class TestBalanceCheck(object):
    
    def test(self,sol):
        assert_equal(sol('[](){([[[]]])}('),False)
        assert_equal(sol('[{{{(())}}}]((()))'),True)
        assert_equal(sol('[[[]])]'),False)
        print ('ALL TEST CASES PASSED')
        
# Run Tests
if __name__ == '__main__':
	t = TestBalanceCheck()
	t.test(balance_check)

	print(timeit.timeit('balance_check("[[[]])]")', setup="from __main__ import balance_check"))
	print(timeit.timeit('balance_check_nostack("[[[]])]")', setup="from __main__ import balance_check_nostack"))


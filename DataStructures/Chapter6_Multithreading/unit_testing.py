# python's standard library provides doctest and unittest
# there is also nose and py.test (3rd party)

# Test Nomenclature

# test fixtures: the code necessary to set up a test (ex: creating an input file for testing and deleting it afterwards)
# test cases: the basic unit of testing
# test suites: the collection of test cases, creates by the subclass unittest.testcase, wher each method has a name beginning with 'test'
# test runner: An object that executes one of more test suites.

# Doctest
	# good for tests inside modules, and functions' 'docstrings'.
	# to use it, we add the following lines in the module:
if __name__ == '__main__':
	import doctest
	doctest.testmod()

# Unittest
	# the standard
	# to use it, the test files should start with test_
import unittest

class BasicsTestCase(unittest.TestCase):
	def test_find_name(self):
		self.assertTrue(1 == 1)
		self.assertFalse(1 == 2)

if __name__ == '__main__':
	unittest.main()

# a fundamental concept here is of TEST ISOLATION, where every test gets a new test object,
	# failure does not stop tests, and tests do not affect each other

# pytest
# pip install pytest
# write a functio that starts with 'test'
def func(x):
	return x + 1
def test_answer():
	assert func(3) == 51
# then run 
# python -m pytest

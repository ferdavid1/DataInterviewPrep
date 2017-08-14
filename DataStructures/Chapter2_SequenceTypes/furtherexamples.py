# reverting strings
def revert(string):
	return string[::-1]

# reversing words
def reversing_words(word):
	new_word = []
	words = word.split(' ')
	for word in words[::-1]:
		new_word.append(word)
	return " ".join(new_word)
print(reversing_words('the best in life'))
# or...
def reversing_words2(word):
	words = word.split()
	return ' '.join(reversed(words))
# or ...
def reversing_words3(word):
	words = word.split()
	words.reverse()
	return ' '.join(words)

#simple string compression
from collections import Counter

def str_comp(s):
	count, last = 1, ''
	list_aux = []
	for i,c in enumerate(s):
		if last == c:
			count += 1
		else:
			if i != 0:
				list_aux.append(str(count))
			list_aux.append(c)
			count = 1
			last = c
	list_aux.append(str(count))
	return ''.join(list_aux)

# string permutation

def perm(str1):
	if len(str1) < 2:
		return str1
	res = []
	for i,c in enumerate(str1):
		for cc in perm(str1[i+1:] + str1[:i]):
			res.append(c + cc)
	return res

# string combination

def combinations(s):
	if len(s) < 2:
		return s
	res = []
	for i,c in enumerate(s):
		res.append(c)
		for j in combinations(s[:1] + s[i+1:]):
			res.append(c + j)
	return res

# palindrome
from collections import defaultdict

def is_palindrome(array):
	array = array.strip(' ')
	if len(array) < 2:
		return True
	if array[0] == array[-1]:
		return is_palindrome(array[1:-1])
	else:
		return False



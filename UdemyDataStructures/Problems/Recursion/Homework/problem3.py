'''
Create a function called word_split, which takes in a string
'phrase' and a set 'list_of_words'. 
The function will then determine if it is possible to split
the string in a way in which words can be made from the list
of words. 
You can assume the phrase will contain words found in the
dictionary if it is completely splittable
'''

def word_split(phrase, words, result=None):

	# result = [] you can't do this, because it will overwrite every recursion!!!
	if not result:
		result = []

	for word in words:
		if phrase.startswith(word):
			result.append(word)
			return word_split(phrase[len(word):], words, result)
	return result

print(word_split('aycaramba', ['ay', 'caramba']))
	
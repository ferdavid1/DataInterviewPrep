#Unicode
print(u'Goodbye\u0020World !')

# joining strings 
slayer = ["Buffy", "Anne", "Summers"]
print(" ".join(slayer))
print("".join(slayer))
print("-<>-".join(slayer))
print("".join(reversed(slayer))) # reversed

#rjust and ljust
name = "Agent Mulder"
print(name.rjust(50, '-'))
print(name.ljust(50, '-'))

# the format() method
print("{0} {1}".format("I'm the One!", "I'm not"))
print("{who} turned {age} this year!".format(who="Buffy", age=17))
print("{who} was {0} this year!".format(12, who="boy"))
print("{} {} {}".format("Python", "can", "count")) # in python 3, you can omit field names

# s, r, and a (using that import decimal)
	# s forces string form
	# r forces representational form
	# a forces representational form but onlt using ASCII characters 
import decimal
print("{0} {0!s} {0!r} {0!a}".format(decimal.Decimal("99.9")))

#string (mapping) unpacking
hero = "Superman"
name = 'kryptonite'
print("Element {name} is {hero}'s proverbial achilles heel".format(**locals()))

#splitlines() method
slayers = "Buffy\nFaith" # '\n makes a new line'
print(slayers.splitlines())

#split(t,n) method
slayers = "Buffy*Slaying-Vamps*16"
fields = slayers.split("*")
print(fields)
job = fields[1].split("-")
print(job)

#use split() to write another method for erasing spaces from strings
def erase_space_from_string(string):
	s1 = erase_space_from_string(" ")
	s2 = "".join(s1)
	return s2

#rsplit() splits string from right to left
wowee = slayers.rsplit("*")
print(wowee)

#strip('chars') method
slayers = "Buffy and Faith999"
print(slayers.strip("999"))

# list every word and the number of times they occer in alphabetical order for some file
import string
import sys

def count_unique_word():
	words = {} # create an empty dictionary
	strip = string.whitespace + string.punctuation + string.digits + "\""
	for filename in sys.argv[1:]:
		with open(filename) as file:
			for line in file:
				for word in line.lower().split():
					word = word.strip(strip)
					if len(word) > 2:
						words[word] = words.get(word,0) + 1
	for word in sorted(words):
		print("'{0}' occurs {1} times".format(word, words[word]))

#lstrip() and rstrip()
print("   Buffy".lstrip()) #strip all leftward whitespace
print("Buffy   ".rstrip()) #strip all rightward whitespace

#swapcase('chars') 
slayers = "Buffy and Faith"
print(slayers.swapcase()) # switch all the cases

capitalize() #makes the first letter of a string uppercase
lower() #makes it all lowercase
upper() #makes it all upper

#index(x) and find(x) - index returns ValueError, find returns -1 on failure to find a character in string. They find the index number of the character, not the character
print(slayers.find("y"))
print(slayers.index("y"))

#count(t, start, end) mothod counts number of occurences of a substring in a string
slayer = "Buffy is a Buffy is a Buffy"
print(slayer.count("Buffy", 0, -1))
print(slayer.count("Buffy"))

#replace(t, u, n) t is the string replaced, u is the replacing, n is the number of times
print(slayer.replace("Buffy", "who", 2)) #replaces twice
print(slayer.replace("Buffy", "who")) # replaces n times



slayer
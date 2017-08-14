#'deep copies'
# copy of a list
	#newList = myList[:]
	#newList2 = list(myList2)	
# copy of a set
people = {"Buffy", "Angel", "Giles"}
slayers = people.copy()
slayers.discard("Giles")
slayers.remove("Angel")
print(slayers)
print(people)
# copy of a dict
	#newDict = myDict.copy()
#copy of another object
	#import copy
	#newObj = copy.copy(myObj) this is a shallow copy
	#newObj2 = copy.deepcopy(myObj2) this is a deep copy


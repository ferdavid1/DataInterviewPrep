t1 = 1234, 'hello!'
print(t1[0])
#t2 = t2, (1,2,3,4,5)

empty = () #create an empty tuple
t1 = 'hello', # make sure to remember the comma, or else it's just a string!
print(len(empty))
print(len(t1))

#count(x)
t = 1,5,7,8,9,4,1,4
print('count : {}'.format(t.count(4)))

#index(x)
t = 1,5,7
print('index: {}'.format(t.index(5)))

#tuple unpacking with the * operator
x, *y = (1,2,3,4)
print(x)
print(y)

#named tuples
	#these are tuples that carry the ability to refer to items by name
import collections
MonsterTuple = collections.namedtuple("Monsters","name age power")
MonsterTuple = ('Vampire', 230, 'immortal')
print(MonsterTuple)
#example:
from collections import namedtuple

def namedtuple_example():
	sunnydale = namedtuple('name', ['job','age'])
	buffy = sunnydale('slayer', '17')
	print(buffy.job)
	print(buffy.age)
if __name__ == '__main__':
	namedtuple_example() #this will print out slayer, because name was set to buffy, job to slayer, and age to 17

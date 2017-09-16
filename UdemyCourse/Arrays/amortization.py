#Amortization
'''
The Strategy of replacing an array with a new, larger array might at first seem slow
A single append operation may require O(n) time to perform
Our new array allows us to add n new elements before the array must be replaced again

Using an algorithmic design patter called amortization, we can show that performing a 
sequence of such append operations on a dynamic array is actually super efficient.

1.) Allocate memory for a larger array of size typically twice the old array
2.) Copy the contents of old array to new array
3.) Free the old array

Initially, array is empty and size is 0.

Insert item 1 (overflow, double the size to 2)
Insert item 2 (overflow, double the size to 4)
Insert item 3 --- everything ok
Insert item 4 (overflow, double the size to 8)
Insert item 5 --- everything ok
Insert item 6 --- everything ok
Insert item 7 --- everything ok
Insert item 8 (overflow, double the size to 16)

Item #          | 1 2 3 4 5 6 7 8 9  10 ...
List size       | 1 2 4 4 8 8 8 8 16 16 ...
Cost            | 1 2 3 1 5 1 1 1 9  1  ...

Amortized Cost: 1+2+3+5+1+1+9+1...      
                ------------------      =   3
                        n           

Amortized Cost is a constant, so O(1)


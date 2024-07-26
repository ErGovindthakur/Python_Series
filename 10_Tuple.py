# A Tuple is an immutable data types in python
 
tuple = () # empty tuple
print(tuple)
tuple = (1,) # tuple with only one element needs a comma
print(tuple)
tuple = (1,2,3) # tuple with more than one element
print(tuple)

# Exploring tuple methods

myTuple = (1,2,2,3,4,5,5,5,6,7,7,7,7,7,8,9,8,8)
print(myTuple.count(2))#.count() method count number of occur
print(myTuple.index(9)) #.index() method returns index of element comes first in tuple

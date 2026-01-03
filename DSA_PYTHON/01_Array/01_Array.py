# import array as arr # importing as alias
from array import *

val = array('i',[1,2,3,4,5,6,7,8,9])

# print(val)

# first way to iterate over array in python
for i in range(0,6): # 0 -> included, 6 -> excluded
     print(val[i], end=" ")
     
print()

# second way to iterate over array
for i in range(len(val)): # 0 -> included, 6 -> excluded
     print(val[i], end=" ")
     
print()
# second way to iterate
for x in val:
     print(x,end=",")

print('\n')

'''
# reverse => it's inbuilt method to reverse array
val.reverse()
# insert elem at specific index
val.insert(1,50)
# append elem at last index
val.append(100)
# modification of elem
val[3] = 99
'''

# copying one array into another array
# copyArray = array(val.typecode,(x for x in val))
copyArray = array(val.typecode,(x*2 for x in val))

copyArray.pop(3) # use when index is known
copyArray.remove(12) # direct remove known elem not by index

# for i in val:
#      print(i,end=" ")

for i in range(len(copyArray)):
     print(copyArray[i],end=",")

print()

arr = array('i',[1,2,3,4,5,6,7,8,9])
# slicing concept
# arr[start index : end index]
print("slicing concept")
abc = arr[2:5] # 2nd index include and 5th index excluded
print(abc) # output =. [3,4,5]

revArr = arr[::-1] # it's a way to reverse array in python using slicing
print(revArr)
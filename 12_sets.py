# Exploring the concept of sets in python
# Note -: Set is the collection of non-repetitive elements

sets = set()
sets.add(1)
sets.add(2)
sets.add(2) # it won't be include in sets bcz it doesn't contain any repeating values
print(sets)

# Properties of sets
'''
1) Sets are unordered 
2) Sets are un indexed
3) Sets can't contain duplicate values
4) There is no way to change items in sets
'''

# Exploring the sets operations

# mySets = {0,1,2,3,4,5,6,7}

# print(len(mySets))
# print(mySets)
# mySets.remove(6)
# print(mySets)
# mySets.pop()
# print(mySets)
# # mySets.clear()
# # print(mySets)
# mySets.union({1,12})
# print(mySets)
# mySets.intersection({1,12})
# print(mySets)


praSet = {1,8,2,3}
print(praSet)

praSet.remove(8)
print(praSet)

praSet.pop()
print(praSet)

praSet.clear()
print(praSet)

setPra = {1,8,2,3}
print(setPra)

union = setPra.union({8,11})
print(union)

intersection = setPra.intersection({8,2})
print(intersection)



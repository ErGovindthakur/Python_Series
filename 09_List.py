# writing the code containing all about list(Array) in python3
# Note -: List are containers used to store a set of values of any data types

fruitList = ['Apple',180,'myFav',True,12.2]
print(fruitList)

#just learn some list method
oddNumber = [1,3,5,7,9];
#Indexing in list
show = oddNumber[0];
print(show)
show = len(oddNumber);
print(show)

#Slicing in odd number
slicing = oddNumber[1:2]
print(slicing)
slicing = oddNumber[0:]
print(slicing)

slicing = oddNumber[:5]
print(slicing)

# Exploring list method
myList = [0,1,2,3,4,5,6,7,8,9]
myList.sort() # sorting
print(myList)
myList.append(10) #appending 10 at last
print(myList)
myList.insert(8,7) # inserting 7 at 8th index
print(myList)
myList.pop(8) # deleting 8th index element
print(myList)
myList.remove(0)
print(myList)
myList.reverse() #reversing
print(myList)





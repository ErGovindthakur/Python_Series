# in python list just behave like dynamic array in other languages

# 1. creating a list and accessing elem
list = [1,2,3,4,5]
print(list[1]) # tmc -> O(1), bcz -> Python directly jumps to memory address

# 2. append (most used one)
list.append(6) # O(1) (amortized)
print(list)

# 3. pop() (remove last)
list.pop()
print(list) # O(1) => no shifting happens

# 4. pop(index) (remove particular index)
list.pop(1) # O(n) => due to shifting

# 5. insert at index
list.insert(len(list),6) # O(n) => elem shift
print(list) 

# 6. remove() by value
list.remove(3) # O(n) => search first and then remove
print(list)

# 7. length
print(len(list)) # O(1), bcz python stores len internally

# 8. Membership check
print(4 in list) # O(n), bcz apply linear search

# 9. sort()
print(list.sort()) # O(n log n) , bcz it's used time sort
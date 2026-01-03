from array import *

# arr = array('typecode',["List of elem"])
arr = array('i',[])

n = int(input("Enter the size of array => "))

elem = (input(f"Enter {n} elem must be integer "))

for i in range(0,n):
     arr.append(int(input(f"num {i+1} -> ")))


print(arr)
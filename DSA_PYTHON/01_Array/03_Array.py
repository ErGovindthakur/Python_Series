from array import *

a1 = array('i',[1,2,3,4,5])

print(a1)

for x in range(0,5):
     print(a1[x],end=" ")
  
print(" ")   
for x in range(len(a1)):
     print(a1[x],end=" ")
     

print(' ')
for x in a1:
     print(x,end=" ")
     

print(" ")
i = 0
while i<len(a1):
     print(a1[i],end=" ")
     i +=1
     
# Array inbuilt methods

print("\nArray in built method")
# 1. append() new elem at last of an array
a1.append(6)
print(a1)

# 2. count() count array elem occurrence
print(a1.count(2))

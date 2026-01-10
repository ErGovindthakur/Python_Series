# Exploring basic program of array in python using list

# 1. Find duplicate elem from the list

def findDup(list):
     if len(list) < 2:
          return list
     
     dupTracker = []

     for i in range(len(list)):
          for j in range(len(list)):
               if i != j and list[i] == list[j]:
                    if list[i] not in dupTracker:
                         dupTracker.append(list[i])
     return dupTracker

print(findDup([1,2,3,1,4,5,3,2]))
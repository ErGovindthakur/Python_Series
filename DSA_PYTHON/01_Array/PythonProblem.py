# Exploring basic program of array in python using list

# 1. Find duplicate elem from the list

def findDup(ls):
     if len(ls) < 2:
          return ls
     
     dupTracker = []
     freq = {}
     # for i in range(len(list)):
     #      for j in range(len(list)):
     #           if i != j and list[i] == list[j]:
     #                if list[i] not in dupTracker:
     #                     dupTracker.append(list[i])
     for num in ls:
          if num in freq:
               freq[num] +=1
               if freq[num] == 2:
                    dupTracker.append(num)
          else:
               freq[num] = 1
     return dupTracker

# print(findDup([1,2,3,1,4,5,3,2]))


# 2. find second largest num from the given array of num

def secondLarge(arr):
     # large = 0
     # sLarge = 0
     large = float('-inf')
     sLarge = float('-inf')
     
     for elem in arr:
          if elem > large:
               sLarge = large
               # print(f"Second Large -> {sLarge}")
               large = elem
               # print(f"Large -> {large}")
          if elem != large and sLarge < elem:
               sLarge = elem
          
     return sLarge

print(secondLarge([1,5,2,8,9,7,10,5])) 
# tmc => O(n) and spc => O(1)
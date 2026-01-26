# Solving two sum II problem using two pointer approach

# 1. Brute force without using two pointer approach

def twoSum1(arr,target):
     if len(arr) < 2:
          return arr
     
     for i in range(len(arr)):
          for j in range(1,len(arr)):
               if arr[i] + arr[j] == target and i != j:
                    return [i,j]
               
     
     return -1

# tmc => O(n^2), spc => O(1)
print(twoSum1([1,2,7,5],7))
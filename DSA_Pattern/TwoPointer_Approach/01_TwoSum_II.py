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
# print(twoSum1([1,2,7,5],7))

# 2. better approach using dict

def twoSum2(arr,target):
     if len(arr)<2:
          return arr
     
     freq = {} # creating empty dict to track elm
     
     for i in range(len(arr)):
          diff = target - arr[i]
          
          if diff in freq:
               return freq[diff],i
          else:
              freq[arr[i]] = i
          
     return -1
# tmc => O(n), spc => O(n)
# print(twoSum2([1,2,7,5],7))

# 3. two pointer approach to solve two sum problem

def twoSumTwoPointer(arr,target):
     if len(arr)<2:
          return arr
     
     st = 0
     end = len(arr)-1
     
     while end > st:
          
          if arr[st] + arr[end] == target:
               return [st, end]
          
          if arr[st]+arr[end] < target:
               st = st+1
          else:
               end = end - 1
     
     return -1

print(twoSumTwoPointer([1,2,7,5],7))
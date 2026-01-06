# exploring lambda best use cases

# 1. Lambda Vs Normal function

# 1. normal function (taken 6 lines of code)
def check_even_odd(x):
     if x % 2 == 0:
          return "Even"
     else:
          return "Odd"

# num = int(input("Enter the number -> "))
# checkResultEvenOdd = check_even_odd(num)
# print(checkResultEvenOdd)

# 2. Lambda function (Only taken three lines)
check_even_odd_2 = lambda x : "Even" if x % 2 == 0 else "Odd"
checkResultEvenOdd2 = check_even_odd_2(10)
# print(checkResultEvenOdd2)

# Most use of lambda with "map","filter","reduce","sorted" inbuilt methods of python

# 1. Lambda with map (gives us exact size only transform list)

nums = [8,7,2,1,9,5]
squareNums = list(map(lambda num : num*num, nums))
print(f"Complete sqr nums are -> {squareNums}")

# 2. Lambda with filter (gives us list based on condition)

filterNums = list(filter(lambda x : x > 5,nums))
print(f"Filtered nums are -> {filterNums}")

# 3. Lambda with reduce (gives us single result)
# Note => We always have to import "reduce" method from "functools" utility

from functools import reduce
reduceNums = reduce(lambda acc,val:acc+val,nums)
print(f"Total reduced nums are -> {reduceNums}")

# 4. Lambda with "sorted" function

students = [("Govind", 90), ("Aman", 85), ("Ravi", 95)]
sortedStudents = sorted(students,key=lambda x : x[1])
print(f"Sorted students list -> {sortedStudents}")

# 5. Normal lambda example find sqr
square = lambda x: x * x
print("Square of num -> ",square(5))
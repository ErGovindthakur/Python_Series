# exploring lambda best use cases

# 1. Lambda Vs Normal function

# 1. normal function (taken 6 lines of code)
def check_even_odd(x):
     if x % 2 == 0:
          return "Even"
     else:
          return "Odd"

num = int(input("Enter the number -> "))
checkResultEvenOdd = check_even_odd(num)
print(checkResultEvenOdd)

# 2. Lambda function (Only taken three lines)
check_even_odd_2 = lambda x : "Even" if x % 2 == 0 else "Odd"
checkResultEvenOdd2 = check_even_odd_2(10)
print(checkResultEvenOdd2)
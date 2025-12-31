''' 
🟢 Question 2 (WHILE LOOP – Condition Based)
🔹 Problem:

Write a program that:

Keeps asking the user to enter a number

Stops when user enters a negative number

Prints the sum of all positive numbers entered
'''

sum = 0
x = 1
while x != 0:
     x = int(input("Enter a number , to stop enter negative number -> "))
     if(x > 0):
          sum += x
     else:
          print("Sum of All positive number ->",sum)
          break
     
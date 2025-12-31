'''
🟢 Question 1 (FOR LOOP – Logic Based)
🔹 Problem:

Write a program to:

Loop from 1 to 20

Print only numbers that are:

Divisible by 3

Not divisible by 5
'''

for i in range(1,20):
     if(i%3==0 and i%5 != 0):
          print(i)
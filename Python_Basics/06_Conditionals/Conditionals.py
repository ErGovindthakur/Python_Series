# Write a Program to find student grading based on their marks

marks = int(input("Enter your marks -> "))

if marks > 30:
     print("pass")
     if marks >80 and marks <= 100:
          print("With Grad Distinct")
     elif marks >= 60 and marks <= 80:
          print("With Grad A")
     elif marks > 50 and marks < 60:
          print("With Grad B")
     else: 
          print("With Grad C")
else:
     print("Fail")
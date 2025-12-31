'''  
Practice Program: Number Analyzer System
What this program will do

The program will:

Take numbers from the user using a loop

Stop when user enters 0

Use a function to analyze each number

For each number, check:

Positive / Negative

Even / Odd

Maintain:

Count of positive numbers

Count of negative numbers

Finally print a summary
'''

def number_analyzer(num):
     if(num > 0):
          if(num % 2 == 0):
               print("even and Positive")
          else:
               print("odd and Positive")
     else:
          if(num % 2 == 0):
               print("even and negative")
          else:
               print("odd and negative")


positiveCount = 0
negativeCount = 0
while True:
     num = int(input("Enter the +ve or -ve number, To stop press Zero -> "))
     
     if(num == 0):
          break
     
     number_analyzer(num)
     
     if(num>0):
          positiveCount += 1
     else:
          negativeCount += 1
          

print("summary\n")
print("Positive number count -> ",positiveCount)
print("Negative number count ->  ",negativeCount)
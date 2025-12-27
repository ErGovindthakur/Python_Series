'''
1. What is a variable?
A variable is a name of memory location that is used to store data.

* Python does not need data type declaration.
'''

name = "Govind"
age = 21
isMale = True

print(name,age,isMale)

# 🔹 Python is Dynamically Typed
x = 10
print("Value of x Before ",x)
x = "Python"
print("Value of x After ",x)


# Same variable, different data type — allowed

'''
Rules for Variable Names
1name     # cannot start with number
my-name   # no hyphen allowed
class     # keyword not allowed
'''

# Assign Multiple Values
a, b, c = 1, 2, 3
print(a,b,c)

# Same value:
x = y = z = 100
print(x,y,z)

# Note -> 
'''
In Python:

There are no primitive data types
Everything is an object
'''

string = "word"
print(type(string))
number = 12
print(type(number))
boolean = True
print(type(boolean))

'''
One-line logic

Variable → reference → object → class
'''
# Learning all about string in python
# Note -: In python the sequences of character enclosed within a single/double/triple quote is called string;

# Example 
name = "Govind";
print(name)
print(type(name));

# Finding the length of string
length = len(name)
print('Length of', name, '= ', length)

# Let's understand the slicing in python string
print(name[0:3]); # Will print value from 0th index to 2nd index

# Negative slicing
print(name[-5:-2]); # Will print value from 1st index to 3rd index
print(name[1: 4]); # Will print value from 1st index to 3rd index

# Understand some tricks
print(name[:4]) # is same as print(name[0:4])
print(name[1:]) # is same as print(name[1:5])

# slicing string with skip functionality
myName = 'GovindThakur';
print(myName[0:11:6]) # output = GT

# String functions

print(len(myName))
print(myName.endswith('r'))
print(myName.startswith('G'))
print(myName.capitalize())

# Escape sequence character

a = 'Govind is a Good boy, \n but not a bad boy. and he says, I\'m giving my best to learn python, \'Govind\''
print(a)
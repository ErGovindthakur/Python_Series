# Q) 1 Write a python program to display a user entered name followed by Good Afternoon using input() function

# user = input('Enter user name ')
# greet = input('Enter the greet time ')
# both = (greet +  ' ' +  user);
# both = (f" {greet}  {user}")
# print(both)

# Q) 2 Write a program to fill "Name" and "Data" in given below template of letter
# letter = '''
# Dear <|Name|>,
# you are selected !
# <|Data|>
# '''

letter = ''' 
Dear <|Name|>,
you are selected !
<|Data|>
'''

print(letter.replace("<|Name|>", "Govind").replace("<|Data|>", "24 September 2025"))

# Q) 3 Write a program to detect double space in a string

name = "Govind is a Good boy and "
print(name.find("  "))

# Q) 4 Replace the double space from problem 3 with a single spaces.

myName = 'Govind  Thakur'
print(myName.replace('  ', ' '))
print(myName.find('  '))
print(myName)

# Q) 5 Write a program to formate the following letter using escape sequence character

# Letter = "Dear Govind, This python course is nice, Thanks !"

letter = " \"Dear Govind\",\n \tThis python course is nice,\n Thanks !"
print(letter)
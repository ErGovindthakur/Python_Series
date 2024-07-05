import pyjokes
import pyttsx3
import os
# Single line comment 
print('Printing jokes.......')

joke = pyjokes.get_joke()
print(joke)

"""
Multi line comment
"""
# Chapter 1 Practice set

# Q) 1  Print twinkle twinkle little star

print('''
SONG LYRICS
Twinkle twinkle little star.
How I wonder what you are.
Up above the world so high.
Like a diamond in the sky.
Twinkle twinkle little star.
How I wonder what you are.

Twinkle twinkle little star.
How I wonder what you are.
Up above the world so high.
Like a diamond in the sky.
Twinkle twinkle little star.
How I wonder what you are.
''')

# Q) 2 Print 5 table using repl in python

'''
>>> 5*1
5
>>> 5*2
10
>>> 5*3
15
>>> 5*4
20
>>> 5*5
25
>>> 5*6
30
>>> 5*7
35
>>> 5*8
40
>>> 5*9
45
>>> 5*10
50
>>>
'''

# Q) 3 Install a external module in python using pip cmd (pyttsx3)
# Here that library is used which convert sentences into speech

engine = pyttsx3.init()
engine.say("Hello Govind work hard , You must be a Millionaire. ")
engine.runAndWait()

# Q) 4 Print all the contents of any particular directory using python like os
# Q) 5 Lebel the content using the single line of comment

# Specify the directory you want to list
directory_path = '/'

# List all files and directories in the specified path
contents = os.listdir(directory_path)

# Print each file and directory name
for item in contents:
     print(item)

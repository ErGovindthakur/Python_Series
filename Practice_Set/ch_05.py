# Q) 1. Write a program to create a dictionary of Hindi words with values of their English translation. Provide user with an option to look it up!
'''
HindiDictionary = {
     "Success":"Kamyab,Safal",
     "Work":"Karya, kaam",
     "Help":"Maddad, Shayta",
     "Self-confidence":"Aatma-Vishwas",
     "Hard-Work":"Kathin-Parishram"
}

search = input(f'{HindiDictionary.keys} Enter the Hindi word ')

print(f'Your searched Hindi Meanings is {search.upper()} and it\'s value is {HindiDictionary[search].upper()}')
'''

# Q) 2. Write a program to display the eight numbers from user and display the unique number once
'''
num1 = int(input('Enter your 1st num'))
num2 = int(input('Enter your 2nd num'))
num3 = int(input('Enter your 3rd num'))
num4 = int(input('Enter your 4th num'))
num5 = int(input('Enter your 5th num'))
num6 = int(input('Enter your 6th num'))
num7 = int(input('Enter your 7th num'))
num8 = int(input('Enter your 8th num'))

# Here we will use the set bcz set doesn't contain any duplicate values

mySet = set()
mySet.add(num1)
mySet.add(num2)
mySet.add(num3)
mySet.add(num4)
mySet.add(num5)
mySet.add(num6)
mySet.add(num7)
mySet.add(num8)

ArrayList = list(mySet)
print(mySet)
'''

#Q) 3. Can we have a set with 18(int) and '18'(str) values in it ?
setCreate = set()
setCreate.add(18)
setCreate.add('18')
print(setCreate)

# Q) 4. What will be the length of following set s : (2)

s = set()
s.add(20)
s.add('20')
s.add(20.0)
print(s)
print(f'Length of set s = {len(s)}')


# Q) 5. What will be the type of empty set
empSet = {} # Output = dic class
print(type(empSet))
empList = []
print(type(empList))
empDictionary = {} # output = dic class
print(type(empDictionary))


# Q) 6. Create an empty dictionary . Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.
'''
favSet = {}
friend1 = favSet.update({
     input('Enter the key'):input('Enter the value')
})
friend2 = favSet.update({
     input('Enter the key'):input('Enter the value')
})
friend4 = favSet.update({
     input('Enter the key'):input('Enter the value')
})
friend4 = favSet.update({
     input('Enter the key'):input('Enter the value')
})
friend5 = favSet.update({
     input('Enter the key'):input('Enter the value')
})
print(favSet)
'''
# Q) 7. If the name of two friends are same; what will happen to the program in the problem 6 ?
'''
Ans-: If the name of two friends are same it will it take only keys acc to their value which will come at last
'''

# Q) 8. If the Language of two friends are same; what will happen to the program in the problem 6 ?
'''
Ans-: If the Language of two friends are same it won't be shown any error instead of that it will print as it is
'''

# Q) 9. Can you change the values inside a list which is contain in set s?
'''
setList = {9,7,12,"Govind", [1,3]} 
print(setList)
Ans) -: It is not possible
'''

# Practice set of List and tuple

# Q) 1. Write a program to store seven fruits in a list entered by the user and stored it into list

# List = []
# user1 = input('Enter the fruits name')
# List.append(user1)
# user2 = input('Enter the fruits name')
# List.append(user2)
# user3 = input('Enter the fruits name')
# List.append(user3)
# user4 = input('Enter the fruits name')
# List.append(user4)
# user5 = input('Enter the fruits name')
# List.append(user5)
# user6 = input('Enter the fruits name')
# List.append(user6)
# user7 = input('Enter the fruits name')
# List.append(user7)
# # for i in range(5):
# #      List.append(user1,user2,user3,user4,user5)
# #      continue
# print(List)

# Q) 2 Write a program to accept marks of 6 students and display them in a sorted manner.
name = 'a';
marks = 1;
studentMarks = [{name:'Ajay', marks:92},
                {name:'Priya', marks:83},
                {name:'Vijay', marks:97},
                {name:'Vinod',marks:99},
                {name:'Suraj',marks:75}
                ]
marks = [90,68,98,89,78]
marks.sort()
print(marks)

# Q) 3. check that a tuple type can't be change in python
checkTuple = (1,2.3,'Good')
# checkTuple[2] = 'Bad'
# print(checkTuple)

# Q) 4. Add the elements of a list
addList = [1,2,3,4,5]
print(sum(addList))

# Q) 5. Write a program to count the number of zeros in the following tuple:
a = (1,2,1,0,0,0,4,5,0,7)
print(a.count(0))








# Learning about input function in python

a = input('Enter the first num : ')

b = input('Enter the second num : ')

# Note Here input function takes the value as string datatype so we cant perform maths ( + , -, *, /)
print('sum of first and second num :', a + b)

# For performing maths we have to convert it into int 

x = int(a)
y = int(b)

print(x, '+', y, '=', x+y)
# Learning all about operators in python

# 1) Arithmetic operator
a = 12
b = 16
c = a + b # Here plus (+ , - , *, /) all are arithmetic operator
print('Addition',c)
c = a - b # Here plus (+ , - , *, /) all are arithmetic operator
print('Subtraction',c)
c = a / b # Here plus (+ , - , *, /) all are arithmetic operator
print('Division',c)
c = a * b # Here plus (+ , - , *, /) all are arithmetic operator
print('Multiplication',c)

# 2) Assignment operator

x = 5 # Here equal to (=) is assignment operator bcz here we are assigning 5 into x
print(x)
x +=3 # Here incrementing 3 and assigning into x
print(x)
x -=3 # Here decrementing 3 and assigning into x
print(x)
x /=3 # Here dividing 3 and assigning into x
print(x)
x *=3 # Here multiplying 3 and assigning into x
print(x)

# 3) Comparison operator (Note -: It always gives output either in true or false)

print(5 == 5) # True
print(5 != 5) # False
print(5 < 5) # False
print(5 <= 5) # True
print(5 > 5) # False
print(5 >= 5) # True

# 4) Logical operator (and, or, not)

# Truth table of or
print('True or True', True or True)
print('True or False', True or False)
print('False or False', False or False)
print('False or True', False or True)

print()

# Truth table of and
print('True and True', True and True)
print('True and False', True and False)
print('False and False', False and False)
print('False and True', False and True)

print()
# Logical not operator
print(not(True)) # output = False
print(not(False)) #output = True

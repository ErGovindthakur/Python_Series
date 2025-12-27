'''
1. What are Data Types?

=> Data types tell Python what kind of data a variable is holding.

=> Since Python is dynamically typed, you don’t declare data types — Python decides them at runtime.
'''

# 2. Main Built-in Data Types (Interview Focused)

##### 1. Numeric Types (Used to store numbers.)
x = 5 # <class 'int'> int
print(type(x))
y = 4.5 # float
print(type(y))
z = 2 + 3j # complex
print(type(z));

##### 2. Text Type (Used to store text.)
name = "Python"
print(type(name)) # <class 'str'>

##### 3. Boolean Type (Used for True / False values.)
is_active = True;
print(type(is_active)) # <class 'bool'>

##### 4. Sequence Types (Used to store multiple values.)

# a) List (mutable)
marks = [45,34,54]
print(type(marks));

# b) Tuple (immutable)
points = (1,2,3)
print(type(points))

# c) Range
nums = range(1,3)
print(nums)
print(type(nums))


##### 5. Set Type (Used to store unique values.)
colors = {"red", "blue", "red"}
print(type(colors))
print(colors)

##### 6. Mapping Type (Stores data in key–value pairs.)
# dictionary (dict)
student = {
     "name":"Ajay",
     "age":22
}
print(student)
print(type(student))

##### 7. None Type (Represents no value.)

x = None
print(x)
print(type(x))

a = (20,)
print(a)
print(type(a))
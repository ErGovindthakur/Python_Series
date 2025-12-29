# "==" checks value equality, while "is" checks whether two variables point to the same object in memory.

num1 = 5
num2 = 5.0

print(num1==num2) # output True (checks only value)
print(num1 is num2) # output False (checks for exact object ref)

# print(num1 is num1) "it is similar" print(<class int> == <class float>) (Wrong Prediction)

# ✅ Correct Analogy

# == → “Do these look the same?”

# is → “Are these literally the same thing?”
## ✅ What is Type Conversion?

* Type conversion means changing one data type into another.

> Example:
```py
"10" → 10
```

### 🔹 Types of Type Conversion
1. 1️⃣ Implicit Type Conversion (Automatic)

Done by Python itself.
```py
x = 10
y = 2.5
z = x + y
print(z)        # 12.5
print(type(z))  # float


# 👉 Python converts int to float
```
2. 2️⃣ Explicit Type Conversion (Manual)

Done by the programmer.
```py
x = "10"
y = int(x)
print(y)
print(type(y))
```

### 🔹 Common Type Casting Functions
Function	Converts To
```py
int()	integer
float()	float
str()	string
bool()	boolean
🔹 Examples (Important)
int("10")     # 10
float("3.5")  # 3.5
str(100)      # "100"
bool(1)       # True
bool(0)       # False
bool("")      # False

# ⚠️ Invalid Conversion (Interview Trap)
int("abc")  # ❌ Error


# Because "abc" is not a number.
```
### 🎯 Interview One-Liner (Type Conversion)

* Type conversion is the process of converting one data type into another, either automatically by Python or manually using built-in functions.
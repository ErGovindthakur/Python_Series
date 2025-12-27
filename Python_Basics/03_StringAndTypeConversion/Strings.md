## ✅ What is a String?

* A string is a sequence of characters used to store text.

> You can create strings using:

* Single quotes ' '

* Double quotes " "

* Triple quotes ''' ''' or """ """

```py
name = "Python"
lang = 'JavaScript'
```

### ✅ Why Strings are Important?

* Store names, messages, data from users

* Used heavily in input/output

* Most common interview topic

### 🔹 String Characteristics

* Strings are immutable (cannot be changed)

* Indexed (supports indexing & slicing)

* Iterable (can loop over characters)

```py
# 🔹 String Indexing
s = "Python"
print(s[0])   # P
print(s[-1])  # n

# 🔹 String Slicing
s = "Python"
print(s[0:4])   # Pyth
print(s[2:])    # thon

# 🔹 String Length
s = "Python"
print(len(s))   # 6

# 🔹 Common String Methods (VERY IMPORTANT)
text = " hello Python "

print(text.upper())     # HELLO PYTHON
print(text.lower())     # hello python
print(text.strip())     # removes spaces
print(text.replace("Python", "World"))
print(text.split())     # ['hello', 'Python']
```
### 🎯 Interview One-Liner (Strings)

* A string in Python is an immutable sequence of characters used to store text data.
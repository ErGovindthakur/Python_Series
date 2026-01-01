# 🐍 Python Exception Handling – Complete Guide (All WH Covered)

This README provides a **complete, interview-ready explanation of Exception Handling in Python**, covering **What, Why, When, How, and Where**, with examples, best practices, and common interview traps.

---

## 1️⃣ What is Exception Handling?

An **exception** is a runtime error that occurs while a program is executing and interrupts the normal flow of the program.

**Exception handling** is the process of handling these runtime errors gracefully so that the program does not crash.

```python
print(10 / 0)   # ZeroDivisionError
```

---

## 2️⃣ Why do we need Exception Handling?

Exception handling is needed to:

* Prevent program crashes
* Handle invalid user input
* Display meaningful error messages
* Make programs robust and user-friendly

Without exception handling, a single error can stop the entire program.

---

## 3️⃣ When should we use Exception Handling?

Use exception handling when:

* Taking user input
* Performing division or type conversion
* Working with files
* Accessing dictionaries or lists
* Communicating with APIs or databases

---

## 4️⃣ How does Exception Handling work?

Python uses the following blocks:

* `try`
* `except`
* `else`
* `finally`

---

## 5️⃣ Basic try–except Syntax

```python
try:
    x = int(input("Enter a number: "))
    print(10 / x)
except:
    print("Something went wrong")
```

---

## 6️⃣ Handling Specific Exceptions (IMPORTANT)

```python
try:
    x = int(input("Enter a number: "))
    print(10 / x)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")
```

👉 Always prefer handling **specific exceptions** instead of using a generic `except`.

---

## 7️⃣ Multiple Exceptions in One Except

```python
try:
    x = int(input("Enter a number: "))
    print(10 / x)
except (ValueError, ZeroDivisionError):
    print("Invalid input or division by zero")
```

---

## 8️⃣ else Block

The `else` block runs **only if no exception occurs**.

```python
try:
    x = int(input("Enter a number: "))
    print(10 / x)
except Exception as e:
    print("Error:", e)
else:
    print("Execution successful")
```

---

## 9️⃣ finally Block (VERY IMPORTANT)

The `finally` block **always executes**, whether an exception occurs or not.

```python
try:
    file = open("test.txt", "r")
except FileNotFoundError:
    print("File not found")
finally:
    print("Done")
```

👉 Used for cleanup operations like closing files or releasing resources.

---

## 🔟 Raising Exceptions (`raise`)

You can manually raise an exception using `raise`.

```python
age = int(input("Enter age: "))

if age < 18:
    raise ValueError("Age must be 18 or above")
```

---

## 1️⃣1️⃣ Exception Object (`as e`)

```python
try:
    print(10 / 0)
except Exception as e:
    print("Error message:", e)
```

---

## 1️⃣2️⃣ Common Built-in Exceptions (Interview Favorite)

| Exception         | Occurs When                     |
| ----------------- | ------------------------------- |
| ZeroDivisionError | Division by zero                |
| ValueError        | Invalid type conversion         |
| TypeError         | Operation on incompatible types |
| IndexError        | List index out of range         |
| KeyError          | Dictionary key not found        |
| FileNotFoundError | File does not exist             |

---

## 1️⃣3️⃣ Where is Exception Handling Used?

* User input validation
* File handling
* Database operations
* Network communication
* Real-world applications

---

## 🎯 Interview One-Liners

**What is exception handling?**

> Exception handling is a mechanism to handle runtime errors and prevent program crashes.

**Difference between error and exception?**

> Errors are serious issues that cannot be handled, whereas exceptions are runtime problems that can be handled.

**Purpose of finally block?**

> The finally block executes regardless of whether an exception occurs.

---

## 🧠 Mini Practice Program

```python
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print(a / b)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Please enter valid numbers")
else:
    print("Calculation successful")
finally:
    print("Program ended")
```

---

✅ **Use this README for interviews, exams, and quick revision.**

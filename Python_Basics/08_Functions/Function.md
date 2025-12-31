# 🐍 Python Functions – Complete Revision (Interview Ready)

This README covers **all important concepts of Python Functions** in a **simple, clear, and practical way**, exactly as discussed.

---

## 1️⃣ What is a Function?

A **function** is a block of reusable code that performs a specific task.

👉 Instead of writing the same code again and again, we define it once and reuse it.

---

## 2️⃣ Why Do We Need Functions?

* Avoid code repetition
* Improve code readability
* Easy debugging and testing
* Break large programs into smaller parts

---

## 3️⃣ Function Syntax

```python
def function_name():
    # code block
```

### Example

```python
def greet():
    print("Hello, Python")

greet()
```

---

## 4️⃣ Function with Parameters

Parameters are inputs passed to a function.

```python
def greet(name):
    print("Hello", name)

greet("Govind")
```

---

## 5️⃣ Function with Return Value

`return` sends a value back to the caller.

```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)
```

⚠️ Code written after `return` does not execute.

---

## 6️⃣ Function with Multiple Parameters

```python
def calculate(a, b):
    print("Sum:", a + b)
    print("Product:", a * b)

calculate(4, 5)
```

---

## 7️⃣ Default Parameters

If no argument is passed, default value is used.

```python
def greet(name="User"):
    print("Hello", name)

greet()
greet("Emma")
```

---

## 8️⃣ Keyword Arguments

Order of arguments does not matter.

```python
def student(name, age):
    print(name, age)

student(age=22, name="Govind")
```

---

## 9️⃣ *args (Variable Length Arguments)

Used when number of arguments is unknown.

```python
def add_all(*args):
    print(sum(args))

add_all(1, 2, 3, 4)
```

---

## 🔟 **kwargs (Keyword Variable Arguments)

Used to pass key-value pairs.

```python
def info(**kwargs):
    print(kwargs)

info(name="Govind", role="Developer")
```

---

## 1️⃣1️⃣ Local vs Global Variables

```python
x = 10   # global variable

def show():
    x = 5   # local variable
    print(x)

show()
print(x)
```

**Output:**

```
5
10
```

---

## 1️⃣2️⃣ Built-in vs User-Defined Functions

* **Built-in functions:** `print()`, `len()`, `type()`
* **User-defined functions:** Created using `def`

---

## 🎯 Interview One-Liners

**What is a function?**

> A function is a reusable block of code that performs a specific task.

**Why are functions used?**

> Functions reduce code duplication and improve readability and maintainability.

**Difference between print and return?**

> `print` displays output, while `return` sends a value back to the caller.

---

## 🧠 Mini Practice Program

```python
def is_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(is_even(10))
```

---

✅ **Use this README for quick revision before interviews or exams.**

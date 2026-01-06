# ⚡ Lambda Functions in Python – Complete Guide (With Interview Questions)

This README explains **Lambda Functions in Python from scratch**, covering **ALL WH aspects** along with **important interview questions and answers**. It is beginner-friendly and interview-ready.

---

## 1️⃣ What is a Lambda Function?

A **lambda function** is a **small, anonymous (nameless) function** written in a **single line**.

👉 In simple words:

> A lambda function is a short function without a name.

---

## 2️⃣ Why do we need Lambda Functions?

Lambda functions are used to:

* Write concise and clean code
* Avoid creating small functions using `def`
* Use functions temporarily
* Improve readability when logic is simple

---

## 3️⃣ When should we use Lambda Functions?

Use lambda functions when:

* Logic is small and simple
* Function is used only once
* Inline functionality is needed

❌ Avoid lambda for complex logic.

---

## 4️⃣ Where are Lambda Functions used?

* `map()`
* `filter()`
* `sorted()`
* `reduce()`
* Functional-style programming
* Data processing

---

## 5️⃣ How does a Lambda Function work?

### Syntax

```python
lambda arguments : expression
```

✔ Can take multiple arguments
✔ Must have only **one expression**
✔ Automatically returns the result

---

## 6️⃣ Lambda vs Normal Function

```python
def add(a, b):
    return a + b

add_lambda = lambda a, b: a + b
```

---

## 7️⃣ Basic Lambda Examples

### Square of a number

```python
square = lambda x: x * x
print(square(5))
```

### Even or Odd

```python
check = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check(7))
```

---

## 8️⃣ Lambda with map()

```python
nums = [1, 2, 3, 4]
result = list(map(lambda x: x * 2, nums))
print(result)
```

---

## 9️⃣ Lambda with filter()

```python
nums = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)
```

---

## 🔟 Lambda with sorted()

```python
students = [("Govind", 90), ("Aman", 85), ("Ravi", 95)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)
```

---

## 1️⃣1️⃣ Lambda with reduce()

```python
from functools import reduce
nums = [1, 2, 3, 4]
total = reduce(lambda a, b: a + b, nums)
print(total)
```

---

## 1️⃣2️⃣ Limitations of Lambda Functions

* Only one expression allowed
* No loops or multiple statements
* Hard to debug if logic is complex

---

# 🎯 Lambda Interview Questions & Answers

---

### Q1. What is a lambda function?

**Answer:**
A lambda function is an anonymous one-line function used for short operations.

---

### Q2. Why are lambda functions used?

**Answer:**
They are used to write small, temporary functions in a concise way.

---

### Q3. Can lambda functions have multiple arguments?

**Answer:**
Yes, lambda functions can take multiple arguments but only one expression.

---

### Q4. Does lambda function return a value?

**Answer:**
Yes, lambda functions automatically return the evaluated expression.

---

### Q5. Can lambda contain loops or multiple statements?

**Answer:**
No, lambda functions support only a single expression.

---

### Q6. Difference between `def` and `lambda`?

**Answer:**
`def` defines a named function with multiple statements, while `lambda` defines an anonymous one-line function.

---

### Q7. Where are lambda functions commonly used?

**Answer:**
With `map()`, `filter()`, `reduce()`, and `sorted()`.

---

### Q8. Is lambda faster than normal function?

**Answer:**
No, lambda functions are not faster; they are just more concise.

---

### Q9. Can lambda functions be reused?

**Answer:**
Yes, if assigned to a variable, but they are usually used once.

---

### Q10. Should lambda functions replace normal functions?

**Answer:**
No, lambda should be used only for small and simple logic.

---

## 🏆 Key Takeaways

* Lambda functions are short and anonymous
* Best for simple and one-time use
* Common in functional programming
* Very important for interviews

---

✅ **Use this README for interview preparation, exams, and quick revision.**

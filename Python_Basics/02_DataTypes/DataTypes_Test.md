# 🧪 Python Data Types – Mini Interview Test

This file contains **exactly the same questions** you practiced, along with **clear, interview‑ready answers** for quick revision.

---

## 🟢 Section A: Conceptual (Very Important)

### Q1. Python is dynamically typed.

👉 What does this mean in simple words?

**Answer:**
Dynamically typed means Python decides the data type of a variable **at runtime**, and we do not need to declare the data type explicitly.

---

### Q2. Why does `print(type(5))` output `<class 'int'>` instead of just `int`?

**Answer:**
Because everything in Python is an **object**, and `5` is an object created from the built‑in class `int`.

---

### Q3. Is `bool` a separate data type in Python?

👉 If yes, from which values is it derived?

**Answer:**
Yes, `bool` is a separate built‑in data type in Python. It represents two values: `True` and `False`. Internally, `bool` is a subclass of `int`.

---

## 🟡 Section B: Predict the Output (Most Asked)

### Q4.

```python
x = 10
y = x
x = 20

print(y)
```

👉 What will be the output and why?

**Answer:**
**Output:** `10`
Because variables store **references to objects**. `y` still refers to the original object `10`, even after `x` is reassigned.

---

### Q5.

```python
colors = {"red", "blue", "red", "green"}
print(colors)
```

👉 How many elements will be printed and why?

**Answer:**
**3 elements** will be printed because a **set stores only unique values** and removes duplicates automatically.

---

### Q6.

```python
nums = range(1, 5)
print(nums)
```

👉 Will this print numbers or something else?

**Answer:**
It will print a **range object**, not the actual numbers. `range()` generates numbers only when iterated.

---

## 🔵 Section C: Identify the Data Type

### Q7.

```python
a = (10)
```

👉 What is the type of `a`?

**Answer:**
`int` — parentheses alone do not create a tuple.

---

### Q8.

```python
b = (10,)
```

👉 What is the type of `b`?

**Answer:**
`tuple` — the comma makes it a tuple.

---

### Q9.

```python
x = None
```

👉 Is `None` the same as `0` or `False`? (Yes/No + Why)

**Answer:**
**No.** `None` represents the absence of a value and is different from `0` or `False`.

---

## 🔴 Section D: True or False (Tricky)

### Q10.

* List is immutable
* Tuple is mutable

👉 True or False?

**Answer:**
❌ List is immutable — **False**
❌ Tuple is mutable — **False**

---

✅ **Use this file for fast revision before interviews.**

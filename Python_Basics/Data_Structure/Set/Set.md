# 🐍 Python Set – Complete Guide (All WH Covered)

This README provides a **complete, interview-ready explanation of Python Sets**, covering **What, Why, When, How, and Where**, along with examples and common interview traps.

---

## 1️⃣ What is a Set?

A **set** is a built-in data structure in Python used to store **multiple unique values** in a single variable.

```python
s = {1, 2, 3, 4}
```

👉 Sets **do not allow duplicate elements**.

---

## 2️⃣ Why do we need a Set?

We use sets when:

* We want **unique elements only**
* We want **fast membership checking**
* Order of elements **does not matter**

Example:

```python
nums = {1, 2, 2, 3}
print(nums)   # {1, 2, 3}
```

---

## 3️⃣ When should we use a Set?

Use a set when:

* Duplicate values must be removed
* You need to perform **mathematical set operations**
* You want faster lookups compared to list or tuple

---

## 4️⃣ How to Create a Set?

### Using curly braces

```python
s = {10, 20, 30}
```

### Using set() constructor

```python
s = set([1, 2, 3, 3])
```

### Empty set (VERY IMPORTANT)

```python
s = set()     # correct
```

❌ Wrong:

```python
s = {}        # dictionary, not set
```

---

## 5️⃣ Where are Sets Used?

* Removing duplicate values
* Membership testing
* Mathematical operations (union, intersection)
* Comparing collections

---

## 6️⃣ Set Properties

| Property          | Supported |
| ----------------- | --------- |
| Ordered           | ❌         |
| Mutable           | ✅         |
| Indexed           | ❌         |
| Allows duplicates | ❌         |
| Heterogeneous     | ✅         |

```python
s = {1, "Python", 3.5, True}
```

---

## 7️⃣ Accessing Set Elements

Sets are **not indexed**, so elements cannot be accessed by position.

❌ Invalid:

```python
s[0]
```

✅ Correct (looping):

```python
for x in s:
    print(x)
```

---

## 8️⃣ Add Elements to Set

### add() – add one element

```python
s.add(40)
```

### update() – add multiple elements

```python
s.update([50, 60])
```

---

## 9️⃣ Remove Elements from Set

### remove() – error if element not found

```python
s.remove(20)
```

### discard() – no error if element not found

```python
s.discard(100)
```

### pop() – removes random element

```python
s.pop()
```

### clear() – removes all elements

```python
s.clear()
```

---

## 🔟 Set Operations (INTERVIEW FAVORITE)

```python
a = {1, 2, 3}
b = {3, 4, 5}
```

### Union

```python
print(a | b)
```

### Intersection

```python
print(a & b)
```

### Difference

```python
print(a - b)
```

### Symmetric Difference

```python
print(a ^ b)
```

---

## 1️⃣1️⃣ Membership Testing

```python
print(3 in a)   # True
```

---

## 1️⃣2️⃣ Common Set Methods

```python
s = {1, 2, 3}

s.copy()
s.pop()
s.clear()
```

---

## 1️⃣3️⃣ Set vs List vs Tuple (Interview Question)

| Feature           | List | Tuple | Set |
| ----------------- | ---- | ----- | --- |
| Ordered           | ✅    | ✅     | ❌   |
| Mutable           | ✅    | ❌     | ✅   |
| Allows duplicates | ✅    | ✅     | ❌   |
| Indexed           | ✅    | ✅     | ❌   |

---

## 🎯 Interview One-Liners

**What is a set?**

> A set is an unordered collection of unique elements in Python.

**Why use set instead of list?**

> To remove duplicates and perform fast membership checks.

**Why set is unordered?**

> Because it stores elements using hashing, not indexing.

---

## 🧠 Mini Practice

```python
nums = [1, 2, 2, 3, 4]
unique_nums = set(nums)
print(unique_nums)
```

---

✅ **Use this README for interviews, exams, and quick revision.**

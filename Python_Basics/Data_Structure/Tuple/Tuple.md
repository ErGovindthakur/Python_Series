# 🐍 Python Tuple – Complete Guide (All WH Covered)

This README provides a **complete, interview-ready explanation of Python Tuples**, covering **What, Why, When, How, and Where**, with clear examples and common traps.

---

## 1️⃣ What is a Tuple?

A **tuple** is a built-in data structure used to store **multiple values** in a **single variable**.

👉 A tuple is **ordered and immutable**.

```python
t = (10, 20, 30)
```

---

## 2️⃣ Why do we need a Tuple?

We use tuples when:

* Data should **not change**
* We want **data safety**
* Slightly **better performance** than lists

Example:

```python
days = ("Mon", "Tue", "Wed")
```

---

## 3️⃣ When should we use a Tuple?

Use a tuple when:

* Data is **fixed**
* No need to add, remove, or update elements
* You want to prevent accidental modification

---

## 4️⃣ How to Create a Tuple?

### Normal tuple

```python
t = (1, 2, 3)
```

### Tuple packing (without parentheses)

```python
t = 1, 2, 3
```

### Single-element tuple (VERY IMPORTANT)

```python
t = (5,)    # correct
```

❌ Wrong:

```python
t = (5)     # int, not tuple
```

---

## 5️⃣ Where are Tuples Used?

* Fixed configuration values
* Database records
* Coordinates (x, y)
* Return multiple values from a function

---

## 6️⃣ Tuple Properties

| Property          | Supported |
| ----------------- | --------- |
| Ordered           | ✅         |
| Immutable         | ✅         |
| Indexed           | ✅         |
| Allows duplicates | ✅         |
| Heterogeneous     | ✅         |

```python
t = (1, "Python", 3.5, True)
```

---

## 7️⃣ Indexing in Tuple

```python
t = (10, 20, 30, 40)
print(t[0])    # 10
print(t[-1])   # 40
```

---

## 8️⃣ Slicing in Tuple

```python
print(t[1:3])   # (20, 30)
print(t[:2])    # (10, 20)
print(t[::2])   # (10, 30)
```

---

## 9️⃣ Tuple is Immutable (MOST IMPORTANT)

```python
t = (1, 2, 3)
t[0] = 10   # ❌ Error
```

👉 Elements of a tuple **cannot be modified**.

---

## 🔟 Tuple with Mutable Object (INTERVIEW FAVORITE)

```python
t = (1, 2, [3, 4])
t[2].append(5)
print(t)
```

**Output:**

```
(1, 2, [3, 4, 5])
```

👉 Tuple is immutable, but it can contain **mutable objects** like lists.

---

## 1️⃣1️⃣ Looping Through a Tuple

```python
t = (10, 20, 30)

for x in t:
    print(x)
```

---

## 1️⃣2️⃣ Tuple Methods

Tuples support only **two built-in methods**:

```python
t = (1, 2, 2, 3)
print(t.count(2))   # 2
print(t.index(3))   # 3
```

---

## 1️⃣3️⃣ Tuple Unpacking

```python
t = (10, 20, 30)
a, b, c = t
print(a, b, c)
```

---

## 1️⃣4️⃣ Tuple vs List (Interview Question)

| Feature | List   | Tuple  |
| ------- | ------ | ------ |
| Mutable | ✅      | ❌      |
| Speed   | Slower | Faster |
| Methods | Many   | Few    |
| Syntax  | []     | ()     |

---

## 🎯 Interview One-Liners

**What is a tuple?**

> A tuple is an ordered and immutable collection used to store fixed data.

**Why tuple is immutable?**

> To ensure data safety and improve performance.

**When should we use tuple instead of list?**

> When data should not be modified.

---

## 🧠 Mini Practice

```python
t = (1, 2, 3, 4)
print(t[1])
print(t[::-1])
```

---

✅ **Use this README for interviews, exams, and quick revision.**

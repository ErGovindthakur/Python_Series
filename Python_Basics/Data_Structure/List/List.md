# 🐍 Python List – Complete Guide (All WH Covered)

This README provides a **complete, interview-ready explanation of Python Lists**, covering **What, Why, When, How, and Where**, along with examples and common traps.

---

## 1️⃣ What is a List?

A **list** is a built-in data structure in Python used to store **multiple values** in a **single variable**.

```python
nums = [1, 2, 3, 4]
```

---

## 2️⃣ Why do we need a List?

* To store multiple related values
* To avoid creating many variables
* To easily iterate, update, add, or remove data

Without list:

```python
a = 10
b = 20
c = 30
```

With list:

```python
nums = [10, 20, 30]
```

---

## 3️⃣ When should we use a List?

Use a list when:

* Data is **ordered**
* Data can **change** (mutable)
* Duplicate values are allowed

```python
marks = [70, 80, 70, 90]
```

---

## 4️⃣ How to Create a List?

### Using square brackets

```python
fruits = ["apple", "banana", "mango"]
```

### Using list() constructor

```python
nums = list((1, 2, 3))
```

---

## 5️⃣ Where are Lists Used?

* Student marks
* Shopping cart items
* API responses
* To-do applications
* Menu-driven programs

---

## 6️⃣ List Properties

| Property          | Supported |
| ----------------- | --------- |
| Ordered           | ✅         |
| Mutable           | ✅         |
| Indexed           | ✅         |
| Allows duplicates | ✅         |
| Heterogeneous     | ✅         |

```python
data = [1, "Python", 3.5, True]
```

---

## 7️⃣ Indexing in List

```python
nums = [10, 20, 30, 40]
print(nums[0])   # 10
print(nums[-1])  # 40
```

---

## 8️⃣ Slicing in List

```python
print(nums[1:3])
print(nums[:2])
print(nums[::2])
```

---

## 9️⃣ Modify List Elements (Mutable)

```python
nums[1] = 25
print(nums)
```

---

## 🔟 Add Elements to List

### append() – add one element

```python
nums.append(50)
```

### extend() – add multiple elements

```python
nums.extend([60, 70])
```

### insert() – add at specific index

```python
nums.insert(1, 15)
```

---

## 1️⃣1️⃣ Remove Elements from List

### remove() – remove by value

```python
nums.remove(25)
```

### pop() – remove by index

```python
nums.pop()
nums.pop(1)
```

### clear() – remove all elements

```python
nums.clear()
```

---

## 1️⃣2️⃣ Length of List

```python
print(len(nums))
```

---

## 1️⃣3️⃣ Looping Through a List

### Using for loop

```python
for x in nums:
    print(x)
```

### Using index

```python
for i in range(len(nums)):
    print(nums[i])
```

---

## 1️⃣4️⃣ Common List Methods (Interview Favorite)

```python
nums = [4, 1, 3, 2]
nums.sort()
nums.reverse()
nums.count(2)
nums.index(3)
```

---

## 1️⃣5️⃣ Copying a List (IMPORTANT)

### ❌ Wrong (reference copy)

```python
a = [1, 2]
b = a
```

### ✅ Correct (shallow copy)

```python
b = a.copy()
b = a[:]
```

---

## 1️⃣6️⃣ List vs Tuple (Interview Question)

| Feature | List   | Tuple  |
| ------- | ------ | ------ |
| Mutable | ✅      | ❌      |
| Speed   | Slower | Faster |
| Syntax  | []     | ()     |

---

## 🎯 Interview One-Liners

**What is a list?**

> A list is an ordered and mutable collection used to store multiple values.

**Why list is mutable?**

> Because its elements can be modified after creation.

**Difference between append and extend?**

> append adds one element, extend adds multiple elements.

---

## 🧠 Mini Practice

```python
nums = [1, 2, 3]
nums.append(4)
nums.remove(2)
print(nums)
```

---

✅ **Use this README for interviews, exams, and revision.**

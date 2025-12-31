# 🐍 Python Dictionary – Complete Guide (All WH Covered)

This README provides a **complete, interview-ready explanation of Python Dictionaries**, covering **What, Why, When, How, and Where**, with clear examples and common interview traps.

---

## 1️⃣ What is a Dictionary?

A **dictionary** is a built-in data structure used to store data in **key–value pairs**.

```python
student = {
    "name": "Govind",
    "age": 22,
    "course": "CSE"
}
```

👉 Keys must be **unique**, values can be duplicated.

---

## 2️⃣ Why do we need a Dictionary?

We use dictionaries when:

* Data is naturally in **key–value form**
* Fast lookup is required
* We want meaningful access using keys instead of indexes

Example:

```python
marks = {"math": 90, "science": 85}
```

---

## 3️⃣ When should we use a Dictionary?

Use a dictionary when:

* You need to map one value to another
* Data needs to be accessed using names/keys
* Order is less important than meaning (Python 3.7+ preserves order)

---

## 4️⃣ How to Create a Dictionary?

### Using curly braces

```python
d = {"a": 1, "b": 2}
```

### Using dict() constructor

```python
d = dict(name="Emma", age=21)
```

### Empty dictionary

```python
d = {}
```

---

## 5️⃣ Where are Dictionaries Used?

* JSON / API data
* User profiles
* Configuration settings
* Database-like records

---

## 6️⃣ Dictionary Properties

| Property              | Supported |
| --------------------- | --------- |
| Ordered (Python 3.7+) | ✅         |
| Mutable               | ✅         |
| Indexed               | ❌         |
| Unique keys           | ✅         |
| Heterogeneous         | ✅         |

---

## 7️⃣ Access Dictionary Values

```python
student = {"name": "Govind", "age": 22}

print(student["name"])
print(student.get("age"))
```

⚠️ `get()` does not raise error if key is missing.

---

## 8️⃣ Add / Update Dictionary Items

```python
student["city"] = "Delhi"     # add
student["age"] = 23             # update
```

---

## 9️⃣ Remove Dictionary Items

```python
student.pop("age")
del student["city"]
student.clear()
```

---

## 🔟 Looping Through Dictionary

```python
for key in student:
    print(key, student[key])

for key, value in student.items():
    print(key, value)
```

---

## 1️⃣1️⃣ Dictionary Methods (Interview Favorite)

```python
student.keys()
student.values()
student.items()
student.update({"age": 25})
```

---

## 1️⃣2️⃣ Dictionary with Mixed Data

```python
data = {
    "id": 1,
    "skills": ["Python", "JS"],
    "active": True
}
```

---

## 1️⃣3️⃣ Nested Dictionary

```python
student = {
    "name": "Govind",
    "marks": {
        "math": 90,
        "science": 85
    }
}
```

---

## 1️⃣4️⃣ Dictionary vs List vs Set

| Feature    | List | Set | Dictionary |
| ---------- | ---- | --- | ---------- |
| Ordered    | ✅    | ❌   | ✅          |
| Mutable    | ✅    | ✅   | ✅          |
| Indexed    | ✅    | ❌   | ❌          |
| Key–Value  | ❌    | ❌   | ✅          |
| Duplicates | ✅    | ❌   | Keys ❌     |

---

## 🎯 Interview One-Liners

**What is a dictionary?**

> A dictionary is a mutable collection that stores data as key–value pairs.

**Why dictionary is faster?**

> Because it uses hashing for fast key lookup.

**Difference between [] and get()?**

> `[]` raises error if key not found, `get()` returns None.

---

## 🧠 Mini Practice

```python
student = {"name": "Govind", "age": 22}
student["age"] = 23

for k, v in student.items():
    print(k, v)
```

---

✅ **Use this README for interviews, exams, and revision.**

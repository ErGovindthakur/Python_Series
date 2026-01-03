# 🐍 Python File Handling – Complete Guide (All WH Covered)

This README provides a **complete, interview-ready explanation of File Handling in Python**, covering **What, Why, When, How, and Where**, along with examples, best practices, and common interview traps.

---

## 1️⃣ What is File Handling?

File handling is the process of **creating, reading, writing, appending, and deleting files** using a program.

Files allow us to **store data permanently** on disk.

```python
print(10 / 0)  # program stops
```

Variables lose data after execution, but **files retain data**.

---

## 2️⃣ Why do we need File Handling?

File handling is required to:

* Store data permanently
* Read and write user information
* Maintain logs and reports
* Handle large data efficiently

Without file handling, data is lost when the program ends.

---

## 3️⃣ When should we use File Handling?

Use file handling when:

* Saving user data
* Reading configuration files
* Logging errors
* Processing reports
* Working with backups

---

## 4️⃣ Where is File Handling used?

* Web applications (logs)
* Banking systems (transactions)
* Student record systems
* Data analysis applications
* Configuration management

---

## 5️⃣ How does File Handling work in Python?

Python provides the built-in function:

```python
open(filename, mode)
```

### Syntax

```python
file = open("data.txt", "r")
```

---

## 6️⃣ File Modes (VERY IMPORTANT)

| Mode | Description                     |
| ---- | ------------------------------- |
| `r`  | Read (file must exist)          |
| `w`  | Write (creates/overwrites file) |
| `a`  | Append (adds data at end)       |
| `x`  | Create new file                 |
| `rb` | Read binary                     |
| `wb` | Write binary                    |

---

## 7️⃣ Reading a File

### Read entire file

```python
file = open("data.txt", "r")
content = file.read()
print(content)
file.close()
```

### Read one line

```python
file = open("data.txt", "r")
print(file.readline())
file.close()
```

### Read all lines

```python
file = open("data.txt", "r")
lines = file.readlines()
print(lines)
file.close()
```

---

## 8️⃣ Writing to a File

```python
file = open("data.txt", "w")
file.write("Hello Python")
file.close()
```

⚠️ `w` mode overwrites existing data.

---

## 9️⃣ Appending to a File

```python
file = open("data.txt", "a")
file.write("\nNew Line Added")
file.close()
```

---

## 🔟 Using `with` Statement (BEST PRACTICE)

```python
with open("data.txt", "r") as file:
    content = file.read()
    print(content)
```

* ✔ Automatically closes file
* ✔ Prevents resource leaks

---

## 1️⃣1️⃣ File Handling with Exception Handling

```python
try:
    with open("test.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found")
```

---

## 1️⃣2️⃣ File Pointer (`tell()` and `seek()`)

```python
file = open("data.txt", "r")
print(file.tell())
file.seek(0)
file.close()
```

---

## 1️⃣3️⃣ Checking if File Exists

```python
import os

if os.path.exists("data.txt"):
    print("File exists")
else:
    print("File not found")
```

---

## 1️⃣4️⃣ Deleting a File

```python
import os
os.remove("data.txt")
```

---

## 🎯 Interview One-Liners

**What is file handling?**

> File handling allows programs to read and write data stored in files.

**Why use `with` statement?**

> It automatically closes files and prevents memory leaks.

**Difference between `w` and `a` mode?**

> `w` overwrites the file, `a` appends data.

---

## ⚠️ Common Interview Traps

* Forgetting to close files
* Using `w` instead of `a`
* Reading a non-existing file without exception handling

---

## 🧠 Mini Practice Program

```python
with open("numbers.txt", "w") as file:
    file.write("1\n2\n3")

with open("numbers.txt", "r") as file:
    print(file.read())
```

---

✅ **Use this README for interviews, exams, and quick revision.**

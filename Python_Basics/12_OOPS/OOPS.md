# 🐍 Object-Oriented Programming (OOP) in Python – Complete Basics

This README explains **OOP in Python from scratch**, in a **simple, interview-ready way**, covering the **core foundations** you must know before moving to advanced OOP concepts.

---

## 1️⃣ What is OOP?

**OOP (Object-Oriented Programming)** is a programming approach where we structure programs using **objects** instead of only functions.

👉 Objects combine **data (attributes)** and **behavior (methods)** together.

---

## 2️⃣ Why do we need OOP?

OOP is used to:

* Organize large programs
* Reuse code efficiently
* Model real-world entities
* Improve readability and maintainability

---

## 3️⃣ Real-World Example

**Student**

* Data: name, age, marks
* Behavior: display(), study(), take_exam()

OOP helps represent this naturally in code.

---

## 4️⃣ Core OOP Concepts

Python OOP is built on these concepts:

1. Class
2. Object
3. Constructor (`__init__`)
4. Encapsulation
5. Inheritance
6. Polymorphism
7. Abstraction

(This README focuses on **Class, Object, Constructor, self**)

---

## 5️⃣ What is a Class?

A **class** is a **blueprint** for creating objects.

```python
class Student:
    pass
```

---

## 6️⃣ What is an Object?

An **object** is an **instance of a class**.

```python
s1 = Student()
```

---

## 7️⃣ Constructor (`__init__`)

The constructor runs **automatically** when an object is created.

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

---

## 8️⃣ Attributes and Methods

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
```

---

## 9️⃣ Creating Objects and Calling Methods

```python
s1 = Student("Govind", 22)
s1.display()
```

**Output:**

```
Name: Govind
Age: 22
```

---

## 🔟 What is `self`? (VERY IMPORTANT)

`self` refers to the **current object**.

When you write:

```python
s1.display()
```

Python internally does:

```python
Student.display(s1)
```

---

## 1️⃣1️⃣ Why use `self`?

* To access object data
* To differentiate between instance variables and local variables
* To bind methods to objects

---

## 🎯 Interview One-Liners

**What is a class?**

> A class is a blueprint for creating objects.

**What is an object?**

> An object is an instance of a class.

**What is a constructor?**

> A constructor initializes object data when an object is created.

**What is `self`?**

> `self` refers to the current object.

---

## 🧠 Mini Practice Example

```python
class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def show(self):
        print(self.brand, self.speed)

c1 = Car("BMW", 120)
c1.show()
```

---

## 🚀 What’s Next in OOP?

* Encapsulation
* Inheritance
* Polymorphism
* Abstraction
* OOP Interview Questions
* Mini OOP Project

---

✅ **Use this README for interviews, exams, and revision.**

# 🧬 Inheritance in Python – Complete Guide (All WH Covered)

This README provides a **complete, interview-ready explanation of Inheritance in Python**, covering **What, Why, When, Where, and How**, with simple examples, real-world analogies, and important interview points.

---

## 1️⃣ What is Inheritance?

**Inheritance** is an Object-Oriented Programming (OOP) concept where **one class (child/subclass)** acquires the **properties and methods** of another class (parent/superclass).

👉 In simple words:

> Inheritance allows a new class to reuse and extend an existing class.

---

## 2️⃣ Why do we need Inheritance?

Inheritance is used to:

* Avoid code duplication
* Promote code reusability
* Improve maintainability
* Extend existing functionality
* Represent real-world relationships

---

## 3️⃣ When should we use Inheritance?

Use inheritance when:

* There is an **IS-A relationship**
* Child class is a specialized version of parent class
* You want to extend parent behavior

✅ Example: Dog is an Animal
❌ Example: Engine is a Car

---

## 4️⃣ Where is Inheritance used?

* Banking applications
* Employee management systems
* Vehicle systems
* Game development
* Frameworks and libraries

---

## 5️⃣ How does Inheritance work in Python?

### Syntax

```python
class Parent:
    pass

class Child(Parent):
    pass
```

---

## 6️⃣ Basic Inheritance Example

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")


d = Dog()
d.speak()   # inherited method
d.bark()    # child method
```

---

## 7️⃣ Types of Inheritance in Python

---

### 1️⃣ Single Inheritance

One parent → one child

```python
class Parent:
    def show(self):
        print("Parent class")

class Child(Parent):
    pass
```

---

### 2️⃣ Multilevel Inheritance

Parent → Child → Grandchild

```python
class A:
    def methodA(self):
        print("Class A")

class B(A):
    def methodB(self):
        print("Class B")

class C(B):
    def methodC(self):
        print("Class C")
```

---

### 3️⃣ Hierarchical Inheritance

One parent → multiple children

```python
class Vehicle:
    def start(self):
        print("Vehicle starts")

class Car(Vehicle):
    pass

class Bike(Vehicle):
    pass
```

---

### 4️⃣ Multiple Inheritance (IMPORTANT)

One child → multiple parents

```python
class Father:
    def skill(self):
        print("Driving")

class Mother:
    def talent(self):
        print("Cooking")

class Child(Father, Mother):
    pass
```

---

## 8️⃣ Method Overriding (VERY IMPORTANT)

Method overriding occurs when a **child class provides its own implementation** of a parent class method.

```python
class Parent:
    def show(self):
        print("Parent method")

class Child(Parent):
    def show(self):
        print("Child method")
```

```python
c = Child()
c.show()   # Child method
```

---

## 9️⃣ super() Keyword (INTERVIEW FAVORITE)

The `super()` keyword is used to call **parent class methods or constructor**.

```python
class Parent:
    def show(self):
        print("Parent method")

class Child(Parent):
    def show(self):
        super().show()
        print("Child method")
```

---

## 🔟 Constructor Inheritance

```python
class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
```

---

## 1️⃣1️⃣ Method Resolution Order (MRO)

MRO defines the **order in which methods are searched** in multiple inheritance.

```python
print(Child.__mro__)
```

---

## 🎯 Interview One-Liners

**What is inheritance?**

> Inheritance allows a class to reuse properties and methods of another class.

**Why is inheritance used?**

> To reduce code duplication and improve reusability.

**What is method overriding?**

> Redefining a parent class method in a child class.

**What is `super()`?**

> Used to access parent class methods and constructors.

---

## ⚠️ Important Interview Notes

* Python supports **multiple inheritance**
* Use inheritance only when an **IS-A relationship** exists
* Improper use can lead to tight coupling

---

## 🧠 Mini Practice Example

```python
class Employee:
    def work(self):
        print("Employee working")

class Developer(Employee):
    def code(self):
        print("Writing code")

d = Developer()
d.work()
d.code()
```

---

## 🏆 Key Takeaways

* Inheritance promotes code reuse
* Child classes extend parent functionality
* `super()` helps reuse parent logic
* Core OOP and interview-critical concept

---

✅ **Use this README for interviews, exams, and revision.**

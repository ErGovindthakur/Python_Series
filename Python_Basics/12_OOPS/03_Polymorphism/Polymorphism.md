# 🔄 Polymorphism in Python – Complete Guide (All WH Covered)

This README provides a **complete, interview-ready explanation of Polymorphism in Python**, covering **What, Why, When, Where, and How**, with simple examples, real-world analogies, and important interview points.

---

## 1️⃣ What is Polymorphism?

**Polymorphism** means **"many forms"**.

In Python, polymorphism allows the **same method name, function, or operator** to behave **differently** depending on the object or context.

👉 In simple words:

> Same action, different behavior.

---

## 2️⃣ Why do we need Polymorphism?

Polymorphism is used to:

* Write flexible and reusable code
* Reduce complexity
* Improve scalability
* Follow clean OOP design principles

---

## 3️⃣ When should we use Polymorphism?

Use polymorphism when:

* Different objects share a common interface
* Same method name but different implementations are required
* Code should work with multiple object types

---

## 4️⃣ Where is Polymorphism used?

* Inheritance-based systems
* UI frameworks
* Payment systems
* Game development
* Plugin architectures

---

## 5️⃣ How does Polymorphism work in Python?

Python supports polymorphism through:

1. Method Overriding
2. Duck Typing
3. Operator Overloading
4. Function Polymorphism

---

## 6️⃣ Method Overriding (MOST IMPORTANT)

Method overriding occurs when a **child class provides its own implementation** of a parent class method.

```python
class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

animals = [Dog(), Cat()]
for animal in animals:
    animal.sound()
```

---

## 7️⃣ Duck Typing (Python-Specific Feature)

Python focuses on **behavior, not object type**.

```python
class Car:
    def move(self):
        print("Car is moving")

class Person:
    def move(self):
        print("Person is walking")

def start(obj):
    obj.move()

start(Car())
start(Person())
```

👉 If an object has the required method, Python accepts it.

---

## 8️⃣ Operator Overloading

The same operator behaves differently based on operands.

```python
print(5 + 5)            # 10
print("Py" + "thon")    # Python
print([1, 2] + [3, 4])  # [1, 2, 3, 4]
```

---

## 9️⃣ Function Polymorphism

The same function works with different data types.

```python
print(len("Python"))
print(len([1, 2, 3]))
print(len((1, 2)))
```

---

## 🔟 Polymorphism with `super()`

```python
class Employee:
    def work(self):
        print("Employee working")

class Developer(Employee):
    def work(self):
        super().work()
        print("Developer writing code")
```

---

## 1️⃣1️⃣ Does Python support Method Overloading?

❌ Python does **not** support traditional method overloading.

✔ It supports **method overriding** and **default arguments** instead.

---

## 🎯 Interview One-Liners

**What is polymorphism?**

> Polymorphism allows the same method name to perform different actions.

**How is polymorphism achieved in Python?**

> Through method overriding, duck typing, operator overloading, and function polymorphism.

**Does Python support method overloading?**

> No, Python supports method overriding, not traditional overloading.

---

## ⚠️ Important Interview Notes

* Python supports **runtime polymorphism**
* Duck typing is a Python-specific strength
* Polymorphism improves extensibility

---

## 🧠 Mini Practice Example

```python
class Shape:
    def area(self):
        pass

class Square(Shape):
    def area(self):
        print("Area = side * side")

class Circle(Shape):
    def area(self):
        print("Area = π * r * r")

shapes = [Square(), Circle()]
for shape in shapes:
    shape.area()
```

---

## 🏆 Key Takeaways

* Polymorphism means many forms
* Same interface, different behavior
* Core OOP and interview-critical concept

---

✅ **Use this README for interviews, exams, and quick revision.**

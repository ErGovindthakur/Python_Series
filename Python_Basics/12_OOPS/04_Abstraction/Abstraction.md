# 🧩 Abstraction in Python – Complete Guide (All WH Covered)

This README provides a **complete, interview-ready explanation of Abstraction in Python**, covering **What, Why, When, Where, and How**, with clear examples, real-world analogies, and important interview points.

---

## 1️⃣ What is Abstraction?

**Abstraction** is an Object-Oriented Programming (OOP) concept that focuses on **hiding internal implementation details** and exposing **only essential features** to the user.

👉 In simple words:

> Abstraction shows *what an object does* instead of *how it does it*.

---

## 2️⃣ Why do we need Abstraction?

Abstraction is needed to:

* Reduce complexity
* Hide unnecessary details
* Improve security
* Enforce a common structure
* Make large systems easy to maintain

---

## 3️⃣ When should we use Abstraction?

Use abstraction when:

* Multiple classes must follow the same blueprint
* You want to enforce implementation rules
* You want to prevent object creation of a base class
* You are designing frameworks or APIs

---

## 4️⃣ Where is Abstraction used?

* Frameworks (Django, Flask)
* APIs
* Payment gateways
* Plugin systems
* Enterprise applications

---

## 5️⃣ How is Abstraction implemented in Python?

Python implements abstraction using:

* **Abstract Base Classes (ABC)**
* **@abstractmethod decorator**

These are provided by the built-in `abc` module.

---

## 6️⃣ Abstract Base Class (ABC)

An abstract class is a class that:

* Contains one or more abstract methods
* Cannot be instantiated directly

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
```

---

## 7️⃣ Abstract Method

An abstract method:

* Has no implementation in the abstract class
* Must be implemented by child classes

```python
class Square(Shape):
    def area(self):
        print("Area = side * side")

class Circle(Shape):
    def area(self):
        print("Area = π * r * r")
```

---

## 8️⃣ Using Abstract Classes

```python
s = Square()
s.area()

c = Circle()
c.area()
```

---

## 9️⃣ What if Abstract Method is Not Implemented?

```python
class Triangle(Shape):
    pass

# t = Triangle()  # ❌ Error
```

👉 Python raises an error, enforcing abstraction rules.

---

## 🔟 Abstract Class with Normal Methods

Abstract classes can contain **both abstract and normal methods**.

```python
class Vehicle(ABC):
    def start(self):
        print("Vehicle started")

    @abstractmethod
    def drive(self):
        pass
```

---

## 1️⃣1️⃣ Abstraction vs Encapsulation (Interview Favorite)

| Feature | Abstraction            | Encapsulation        |
| ------- | ---------------------- | -------------------- |
| Focus   | What object does       | How data is accessed |
| Hides   | Implementation details | Data                 |
| Uses    | ABC, abstract methods  | Private variables    |

---

## 🎯 Interview One-Liners

**What is abstraction?**

> Abstraction hides implementation details and exposes only essential features.

**How is abstraction achieved in Python?**

> Using abstract base classes and abstract methods.

**Can we create object of abstract class?**

> No, abstract classes cannot be instantiated.

---

## ⚠️ Important Interview Notes

* Python supports **partial abstraction**
* Abstract class may contain normal methods
* All abstract methods must be overridden in child classes

---

## 🧠 Mini Practice Example

```python
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass

class UPI(Payment):
    def pay(self):
        print("Payment via UPI")

class Card(Payment):
    def pay(self):
        print("Payment via Card")

payments = [UPI(), Card()]
for p in payments:
    p.pay()
```

---

## 🏆 Key Takeaways

* Abstraction focuses on *what*, not *how*
* Enforces structure and consistency
* Final core pillar of OOP

---

✅ **Use this README for interviews, exams, and quick revision.**

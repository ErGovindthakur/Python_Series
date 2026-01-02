# 🔐 Encapsulation in Python – Complete Guide (All WH Covered)

This README provides a **complete, interview-ready explanation of Encapsulation in Python**, covering **What, Why, When, Where, and How**, with simple examples and real-world relevance.

---

## 1️⃣ What is Encapsulation?

**Encapsulation** is an OOP concept that means **wrapping data (variables) and methods (functions) together inside a class** and **restricting direct access** to some of the object’s data.

👉 In simple words:

> Encapsulation protects data from direct access and misuse.

---

## 2️⃣ Why do we need Encapsulation?

Encapsulation is important because it:

* Protects sensitive data
* Prevents accidental modification
* Controls how data is accessed or updated
* Makes code more secure and maintainable

---

## 3️⃣ When should we use Encapsulation?

Use encapsulation when:

* Data should not be accessed directly
* Validation is required before updating values
* You are modeling real-world entities like Bank, User, Employee

---

## 4️⃣ Where is Encapsulation used?

* Banking systems
* Login & authentication systems
* APIs
* Enterprise-level applications
* Real-world business logic

---

## 5️⃣ How does Encapsulation work in Python?

Python achieves encapsulation using **access modifiers (by convention)**:

| Access Level | Syntax       | Meaning                              |
| ------------ | ------------ | ------------------------------------ |
| Public       | `variable`   | Accessible everywhere                |
| Protected    | `_variable`  | Accessible within class & subclasses |
| Private      | `__variable` | Accessible only inside the class     |

---

## 6️⃣ Public Members

Public members can be accessed from anywhere.

```python
class Student:
    def __init__(self, name):
        self.name = name

s = Student("Govind")
print(s.name)   # Allowed
```

---

## 7️⃣ Protected Members (`_variable`)

Protected members should **not be accessed directly**, but Python does not restrict it.

```python
class Student:
    def __init__(self, marks):
        self._marks = marks

s = Student(85)
print(s._marks)   # Allowed but discouraged
```

👉 `_` indicates: *internal use only*.

---

## 8️⃣ Private Members (`__variable`) – MOST IMPORTANT

Private members restrict direct access using **name mangling**.

```python
class Student:
    def __init__(self, marks):
        self.__marks = marks

s = Student(90)
# print(s.__marks)  # ❌ Error
```

---

## 9️⃣ Name Mangling in Python

Python internally renames private variables:

```python
print(s._Student__marks)  # Works
```

👉 This prevents **accidental access**, not forced access.

---

## 🔟 Accessing Private Data using Methods (BEST PRACTICE)

```python
class Student:
    def __init__(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, new_marks):
        if new_marks >= 0:
            self.__marks = new_marks
        else:
            print("Invalid marks")
```

```python
s = Student(80)
print(s.get_marks())
s.set_marks(90)
print(s.get_marks())
```

✔ Controlled access
✔ Validation applied
✔ Data protected

---

## 1️⃣1️⃣ Real-World Example (Bank Account)

```python
class Bank:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def show_balance(self):
        print("Balance:", self.__balance)
```

---

## 🎯 Interview One-Liners

**What is encapsulation?**

> Encapsulation is binding data and methods together and restricting direct access to data.

**Why encapsulation is important?**

> It improves data security and code maintainability.

**How is encapsulation achieved in Python?**

> By using private and protected variables with controlled access methods.

---

## ⚠️ Important Interview Note

> Python does not have true private variables; it uses name mangling for data hiding.

---

## 🧠 Mini Practice Task

Create a class `Employee` with:

* private salary
* `get_salary()` and `set_salary()` methods

---

## 🏆 Key Takeaways

* Encapsulation protects data
* Use `__variable` for private data
* Always access private data using methods
* Essential for real-world applications

---

✅ **Use this README for interviews, exams, and revision.**

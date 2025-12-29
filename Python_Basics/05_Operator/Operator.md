## What is an Operator and what are the requirements in Programming Languages ?
* Operators are symbols used to perform operations on data, and they are required to calculate values, make decisions, compare data, and control program logic.

## 🧪 Python Operators – Interview Revision (Twisted Questions Focus)

This README covers **all Python operators** with **short explanations, examples, and common interview traps**. Use it for **quick revision before interviews**.

---

## 1️⃣ Arithmetic Operators

| Operator | Meaning                 |
| -------- | ----------------------- |
| `+`      | Addition                |
| `-`      | Subtraction             |
| `*`      | Multiplication          |
| `/`      | Division (always float) |
| `//`     | Floor division          |
| `%`      | Modulus                 |
| `**`     | Power                   |

### 🔹 Twisted Questions

```python
print(5 / 2)    # 2.5
print(5 // 2)   # 2
print(-5 // 2)  # -3 (floor, not truncation)
print(2 ** 3)   # 8
```

---

## 2️⃣ Assignment Operators

| Operator | Example |
| -------- | ------- |
| `=`      | x = 5   |
| `+=`     | x += 2  |
| `-=`     | x -= 2  |
| `*=`     | x *= 2  |
| `/=`     | x /= 2  |

### 🔹 Twisted Question

```python
x = 5
x += 3
print(x)  # 8
```

---

## 3️⃣ Comparison (Relational) Operators

| Operator | Meaning          |
| -------- | ---------------- |
| `==`     | Equal to         |
| `!=`     | Not equal        |
| `>`      | Greater than     |
| `<`      | Less than        |
| `>=`     | Greater or equal |
| `<=`     | Less or equal    |

### 🔹 Twisted Questions

```python
print(5 == 5.0)   # True
print(5 is 5.0)   # False
print(10 > 5 > 3) # True (chaining)
```

---

## 4️⃣ Logical Operators

| Operator | Meaning           |
| -------- | ----------------- |
| `and`    | Both true         |
| `or`     | At least one true |
| `not`    | Reverse result    |

### 🔹 Twisted Questions

```python
print(True and False)   # False
print(True or False)    # True
print(not True)         # False
print(0 and 5)          # 0
print(5 and 10)         # 10
print(0 or 7)           # 7

# Note
'''
and
Returns first falsy value
If none → returns last operand

or
Returns first truthy value
If none → returns last operand

'''
```

---

## 5️⃣ Bitwise Operators (Basics)

| Operator | Meaning     |    |
| -------- | ----------- | -- |
| `&`      | AND         |    |
| `        | `           | OR |
| `^`      | XOR         |    |
| `~`      | NOT         |    |
| `<<`     | Left shift  |    |
| `>>`     | Right shift |    |

### 🔹 Example

```python
print(5 & 3)   # 1
print(5 | 3)   # 7
```

---

## 6️⃣ Membership Operators

| Operator | Meaning     |
| -------- | ----------- |
| `in`     | Present     |
| `not in` | Not present |

### 🔹 Twisted Questions

```python
print('a' in 'cat')        # True
print(1 in [True, 2, 3])  # True (True == 1)
```

---

## 7️⃣ Identity Operators (VERY IMPORTANT)

| Operator | Meaning          |
| -------- | ---------------- |
| `is`     | Same object      |
| `is not` | Different object |

### 🔹 Twisted Questions

```python
a = [1, 2]
b = [1, 2]
print(a == b)  # True
print(a is b)  # False

x = 256
y = 256
print(x is y)  # True (integer caching)
```

---

## 8️⃣ Operator Precedence (Common Trap)

```python
print(10 + 2 * 3)    # 16
print((10 + 2) * 3)  # 36
print(not True == False)  # True
```

---

## 🎯 Interview Golden Rules

* Use `==` to compare values
* Use `is` to compare identity
* `/` always returns float
* `and` / `or` return values, not booleans
* Negative floor division surprises many candidates

---

✅ **Revise this README to handle twisted operator questions confidently.**

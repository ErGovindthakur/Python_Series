# 🧪 Python Operators – Practical Test (With Output & Explanation)

This README contains **exactly the same 10 operator questions**, along with **correct output and simple explanations** for quick revision.

---

## 🟢 Q1. Predict the Output

```python
print(10 + 3 * 2)
```

**Output:**

```
16
```

**Explanation:**
Multiplication (`*`) has higher precedence than addition (`+`). So `3 * 2 = 6`, then `10 + 6 = 16`.

---

## 🟢 Q2. Predict the Output

```python
print(5 // 2)
print(-5 // 2)
```

**Output:**

```
2
-3
```

**Explanation:**
`//` is floor division. It returns the greatest integer less than or equal to the result.

* `5 / 2 = 2.5 → floor = 2`
* `-5 / 2 = -2.5 → floor = -3`

---

## 🟢 Q3. Predict the Output

```python
print(0 and 10)
print(10 and 0)
print(10 and 20)
```

**Output:**

```
0
0
20
```

**Explanation:**
`and` returns the first falsy value. If all values are truthy, it returns the last value.

---

## 🟢 Q4. Predict the Output

```python
print(0 or 5)
print(5 or 0)
print(0 or 0)
```

**Output:**

```
5
5
0
```

**Explanation:**
`or` returns the first truthy value. If no truthy value exists, it returns the last value.

---

## 🟢 Q5. Predict the Output

```python
print(5 == 5.0)
print(5 is 5.0)
```

**Output:**

```
True
False
```

**Explanation:**
`==` compares values, so `5` and `5.0` are equal.
`is` checks memory identity, and `int` and `float` are different objects.

---

## 🟢 Q6. Predict the Output

```python
a = [1, 2]
b = a
c = [1, 2]

print(a == b)
print(a is b)
print(a == c)
print(a is c)
```

**Output:**

```
True
True
True
False
```

**Explanation:**
`==` compares values, `is` compares object identity. `b` refers to the same list as `a`, but `c` is a different list.

---

## 🟢 Q7. Predict the Output

```python
print(not 5)
print(not 0)
```

**Output:**

```
False
True
```

**Explanation:**
Non-zero values are truthy. `not` reverses the boolean value.

---

## 🟢 Q8. Predict the Output

```python
print(10 > 5 > 2)
print(10 > 5 < 2)
```

**Output:**

```
True
False
```

**Explanation:**
Python supports chained comparisons.
`10 > 5 > 2` means `10 > 5 and 5 > 2`.

---

## 🟢 Q9. Predict the Output

```python
print(True + True)
print(True * 5)
```

**Output:**

```
2
5
```

**Explanation:**
In Python, `True` is treated as `1` and `False` as `0` in arithmetic operations.

---

## 🟢 Q10. What will happen?

```python
print(10 / 0)
```

**Output:**

```
ZeroDivisionError
```

**Explanation:**
Division by zero is not allowed in Python, so it raises a runtime error.

---

✅ **Use this file for fast revision of operator-based interview questions.**

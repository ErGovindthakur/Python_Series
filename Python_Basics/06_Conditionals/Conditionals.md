## ✅ What is if–else?

* if–else is used to make decisions in a program.

* 👉 It helps the program decide what to do based on a condition.

```py
if condition:
    # code runs if condition is True
else:
    # code runs if condition is False

# ⚠️ Indentation is mandatory in Python (no {}).
```

### 🟢 Simple Example
```py
age = 20

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")
```

## 🔹 How Python evaluates condition

* Condition must return True or False

* Uses comparison operators (> < == != >= <=)

* Uses logical operators (and or not)

## 🟢 if – elif – else (Multiple Conditions)
```py
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Grade C")

'''
* 👉 Python checks top to bottom
* 👉 First True block runs
* 👉 Others are skipped
'''
```

## 🟢 Nested if (if inside if)
```py
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Allowed")
    else:
        print("ID required")
else:
    print("Not allowed")
```


##  🟢 Short-hand if (Ternary Operator)
```py
age = 17
print("Adult") if age >= 18 else print("Minor")


# ✔️ Useful for single-line conditions
```

## 🔴 Truthy & Falsy in if–else (IMPORTANT)

> Python treats these as False:

* 0

* ""

* []

* None

* False

> Everything else is True.

```py
if 0:
    print("Yes")
else:
    print("No")   # runs
```
## What is a loop?

* A loop is used to execute a block of code repeatedly based on a condition.

### Difference between for and while?

* "for" is used when iterations are known, "while" is used when condition-based repetition is needed.


### 1.  For Loop
```py
# Basic Syntax
for variable in sequence:
    # code block
```
### Example -> Print the numbers
```py
for i in range(1, 6):
    print(i)

# Example 2 -> (Example 2: Loop through a string
name = "Python"

for ch in name:
    print(ch))


# Example 3: Loop through a list
nums = [10, 20, 30]

for n in nums:
    print(n)

```

### 2. while Loop
* Use while loop when repetition depends on a condition.

```py
# Basic syntax
while condition:
    # code block


# Example 1. (print numbers)
i = 1
while i <= 5:
    print(i)
    i += 1


# Example 2: Input-based loop
x = 1
while x != 0:
    x = int(input("Enter number (0 to stop): "))
```

### 3. Loop Control Statements (VERY IMPORTANT)

```py
# 1️⃣ break – stop the loop
for i in range(1, 6):
    if i == 3:
        break
    print(i)
'''
output
1
2
'''

# 2️⃣ continue – skip current iteration
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

'''
output
1
2
4
5
'''

# 3️⃣ pass – do nothing (placeholder)
for i in range(5):
    pass
```

## INTERVIEW TRAP

```py
#1.  else with Loops
for i in range(3):
    print(i)
else:
    print("Loop finished")
# Runs else only if loop completes normally (no break).

# 2. Nested Loops
for i in range(1, 4):
    for j in range(1, 3):
        print(i, j)
```

### 🧠 Common Interview Traps

* Forgetting to update variable in while loop → infinite loop

* Confusing break and continue

* Loop else misunderstanding
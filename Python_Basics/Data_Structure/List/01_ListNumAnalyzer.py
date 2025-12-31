'''
🧩 Practice Problem: List Number Analyzer
🔹 Problem Statement

* Write a program that:

1. Takes numbers from the user and stores them in a list

2. Stops taking input when the user enters 0

3. After input is done, the program should:

-> Print the list of numbers

-> Print the sum of all numbers

-> Print the largest number

-> Print the smallest number

-> Count how many numbers are even and odd
'''
nums = []
even_count = 0
odd_count = 0

while True:
    n = int(input("Enter number (0 to stop): "))

    if n == 0:
        break

    nums.append(n)

    if n % 2 == 0:
        even_count += 1
    else:
        odd_count += 1


if nums:
    print("Numbers:", nums)
    print("Max:", max(nums))
    print("Min:", min(nums))
    print("Sum:", sum(nums))
    print("Even count:", even_count)
    print("Odd count:", odd_count)
else:
    print("No numbers entered")

def two_sum_bruteforce(arr, target):
    """
    Brute Force Approach
    Works for any array (sorted or unsorted)

    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    n = len(arr)

    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                return [i, j]

    return -1


def two_sum_hashmap(arr, target):
    """
    Hash Map (Dictionary) Approach
    Best general solution for unsorted arrays

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    seen = {}

    # for i, num in enumerate(arr):
    for i in range(len(arr)):
        # print(f"num -> {arr[i]}, i -> {i}")
        diff = target - arr[i]

        if diff in seen:
            return [seen[diff], i]

        seen[arr[i]] = i
        # print(f"seen -> {i} , {seen}")
    return -1


def two_sum_two_pointer(arr, target):
    """
    Two Pointer Approach
    Array MUST be sorted

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    left = 0
    right = len(arr) - 1

    while left < right:
        s = arr[left] + arr[right]

        if s == target:
            return [left, right]
        elif s < target:
            left += 1
        else:
            right -= 1

    return -1


# -------------------------------
# Example Usage
# -------------------------------

nums_unsorted = [1, 2, 7, 5]
nums_sorted = [1, 2, 5, 7]
target = 7

print("Brute Force:", two_sum_bruteforce(nums_unsorted, target))
print("Hash Map   :", two_sum_hashmap(nums_unsorted, target))
print("Two Pointer:", two_sum_two_pointer(nums_sorted, target))

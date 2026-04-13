# TASK 3
print("NIVASRI T | 24BAD081")
import random
import time
# Brute Force
def max_subarray_bruteforce(arr):
    n = len(arr)
    max_sum = float('-inf')

    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]
            max_sum = max(max_sum, current_sum)
    return max_sum
# Divide and Conquer
def max_cross(arr, left, mid, right):
    left_sum = float('-inf')
    total = 0

    for i in range(mid, left - 1, -1):
        total += arr[i]
        left_sum = max(left_sum, total)

    right_sum = float('-inf')
    total = 0

    for i in range(mid + 1, right + 1):
        total += arr[i]
        right_sum = max(right_sum, total)

    return left_sum + right_sum
def max_subarray_dc(arr, left, right):
    if left == right:
        return arr[left]
    mid = (left + right) // 2
    left_max = max_subarray_dc(arr, left, mid)
    right_max = max_subarray_dc(arr, mid + 1, right)
    cross_max = max_cross(arr, left, mid, right)

    return max(left_max, right_max, cross_max)
# Generate random array
arr = [random.randint(-100, 100) for _ in range(10000)]
# Measure Brute Force
start = time.time()
max_subarray_bruteforce(arr)
end = time.time()
print("Brute Force Time:", end - start)
# Measure Divide & Conquer
start = time.time()
max_subarray_dc(arr, 0, len(arr)-1)
end = time.time()
print("Divide & Conquer Time:", end - start)

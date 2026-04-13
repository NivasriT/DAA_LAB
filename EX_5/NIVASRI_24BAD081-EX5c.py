print("NIVASRI T | 24BAD081")
import time

# Recursive Binary Search
def binary_recursive(arr, low, high, key):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == key:
        return mid
    elif key < arr[mid]:
        return binary_recursive(arr, low, mid - 1, key)
    else:
        return binary_recursive(arr, mid + 1, high, key)


# Iterative Binary Search
def binary_iterative(arr, key):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif key < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1


# Linear Search
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


# Main
n = 1000000
arr = list(range(n))   # Sorted array
key = n - 1            # Last element

start = time.time()
binary_recursive(arr, 0, n - 1, key)
print("Recursive Binary Time:", time.time() - start)

start = time.time()
binary_iterative(arr, key)
print("Iterative Binary Time:", time.time() - start)

start = time.time()
linear_search(arr, key)
print("Linear Search Time:", time.time() - start)

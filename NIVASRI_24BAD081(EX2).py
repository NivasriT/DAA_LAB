print("NIVASRI T | 24BAD081")
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# ---- Main Program ----
n = int(input("Enter number of elements: "))
arr = []

print("Enter elements:")
for i in range(n):
    arr.append(int(input()))

key = int(input("Enter element to search: "))

# Linear Search
result = linear_search(arr, key)
if result != -1:
    print("Linear Search: Element found at index", result)
else:
    print("Linear Search: Element not found")

# Binary Search (list must be sorted)
arr.sort()
result = binary_search(arr, key)
if result != -1:
    print("Binary Search: Element found at index", result)
else:
    print("Binary Search: Element not found")

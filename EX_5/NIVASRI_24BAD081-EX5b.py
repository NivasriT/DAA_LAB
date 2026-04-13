print("NIVASRI T | 24BAD081")
import random
import sys
# Increase recursion limit (just in case)
sys.setrecursionlimit(3000)
# Quick Sort (Last Element Pivot)
def partition(arr, low, high):
    global comparisons
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        comparisons += 1
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
# Randomized Quick Sort
def randomized_partition(arr, low, high):
    random_index = random.randint(low, high)
    arr[random_index], arr[high] = arr[high], arr[random_index]
    return partition(arr, low, high)


def randomized_quick_sort(arr, low, high):
    if low < high:
        pi = randomized_partition(arr, low, high)
        randomized_quick_sort(arr, low, pi - 1)
        randomized_quick_sort(arr, pi + 1, high)
# Performance Test
n = 2000
sorted_array = list(range(n))

# Test Normal Quick Sort
arr1 = sorted_array.copy()
comparisons = 0
try:
    quick_sort(arr1, 0, n - 1)
    print("Normal Quick Sort Comparisons:", comparisons)
except RecursionError:
    print("Normal Quick Sort hit recursion limit!")
# Test Randomized Quick Sort
arr2 = sorted_array.copy()
comparisons = 0

randomized_quick_sort(arr2, 0, n - 1)
print("Randomized Quick Sort Comparisons:", comparisons)

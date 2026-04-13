print("NIVASRI T | 24BAD081")
# Global variable to track maximum recursion depth
max_depth = 0
def merge(arr, left, mid, right):
    # Create temporary arrays
    L = arr[left:mid+1]
    R = arr[mid+1:right+1]

    i = j = 0
    k = left

    # Merge two sorted halves
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy remaining elements
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1


def merge_sort(arr, left, right, depth):
    global max_depth
    
    # Update maximum depth
    if depth > max_depth:
        max_depth = depth

    if left < right:
        mid = (left + right) // 2
        
        merge_sort(arr, left, mid, depth + 1)
        merge_sort(arr, mid + 1, right, depth + 1)
        merge(arr, left, mid, right)


# Main Program
arr = list(map(int, input("Enter elements separated by space: ").split()))

merge_sort(arr, 0, len(arr) - 1, 1)

print("Sorted array:", arr)
print("Maximum Recursion Depth:", max_depth)

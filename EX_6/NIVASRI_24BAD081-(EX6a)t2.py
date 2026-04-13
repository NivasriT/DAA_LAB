# TASK 2
print("NIVASRI T | 24BAD081")
def max_cross(arr, left, mid, right):
    left_sum = float('-inf')
    total = 0
    max_left = mid

    for i in range(mid, left - 1, -1):
        total += arr[i]
        if total > left_sum:
            left_sum = total
            max_left = i

    right_sum = float('-inf')
    total = 0
    max_right = mid + 1

    for i in range(mid + 1, right + 1):
        total += arr[i]
        if total > right_sum:
            right_sum = total
            max_right = i

    return left_sum + right_sum, max_left, max_right
def max_subarray_dc(arr, left, right):
    if left == right:
        return arr[left], left, right

    mid = (left + right) // 2

    left_sum, l_start, l_end = max_subarray_dc(arr, left, mid)
    right_sum, r_start, r_end = max_subarray_dc(arr, mid + 1, right)
    cross_sum, c_start, c_end = max_cross(arr, left, mid, right)

    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_sum, l_start, l_end
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return right_sum, r_start, r_end
    else:
        return cross_sum, c_start, c_end
# Test
arr = [2, -4, 3, -1, 2, -4, 3]
result, start, end = max_subarray_dc(arr, 0, len(arr)-1)
print("Maximum Sum:", result)
print("Start Index:", start)
print("End Index:", end)
print("Subarray:", arr[start:end+1])

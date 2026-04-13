# Task 3: Padding for non power of 2
print("NIVASRI T | 24BAD081")
def add(A, B):
    n = len(A)
    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]
def sub(A, B):
    n = len(A)
    return [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]
def strassen(A, B):
    n = len(A)
    if n == 1:
        return [[A[0][0] * B[0][0]]]
    mid = n // 2
    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]
    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]
    M1 = strassen(add(A11, A22), add(B11, B22))
    M2 = strassen(add(A21, A22), B11)
    M3 = strassen(A11, sub(B12, B22))
    M4 = strassen(A22, sub(B21, B11))
    M5 = strassen(add(A11, A12), B22)
    M6 = strassen(sub(A21, A11), add(B11, B12))
    M7 = strassen(sub(A12, A22), add(B21, B22))
    C11 = add(sub(add(M1, M4), M5), M7)
    C12 = add(M3, M5)
    C21 = add(M2, M4)
    C22 = add(sub(add(M1, M3), M2), M6)
    new = []
    for i in range(mid):
        new.append(C11[i] + C12[i])
    for i in range(mid):
        new.append(C21[i] + C22[i])
    return new
def next_power_of_2(n):
    power = 1
    while power < n:
        power *= 2
    return power
def pad_matrix(A, size):
    n = len(A)
    new = [[0]*size for _ in range(size)]
    for i in range(n):
        for j in range(n):
            new[i][j] = A[i][j]
    return new
def unpad_matrix(A, size):
    return [row[:size] for row in A[:size]]
# Example 3x3 matrices
A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[9,8,7],[6,5,4],[3,2,1]]
n = len(A)
m = next_power_of_2(n)
A_pad = pad_matrix(A, m)
B_pad = pad_matrix(B, m)
C_pad = strassen(A_pad, B_pad)
C = unpad_matrix(C_pad, n)
print("Result for non-power of 2 matrix:")
print(C)

print("NIVASRI T | 24BAD081")
# Task 1: Naive and Strassen Multiplication
# -------- Naive Multiplication --------
def naive_multiply(A, B):
    n = len(A)
    C = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C
# -------- Strassen Multiplication --------
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
    # 7 multiplications
    M1 = strassen(add(A11, A22), add(B11, B22))
    M2 = strassen(add(A21, A22), B11)
    M3 = strassen(A11, sub(B12, B22))
    M4 = strassen(A22, sub(B21, B11))
    M5 = strassen(add(A11, A12), B22)
    M6 = strassen(sub(A21, A11), add(B11, B12))
    M7 = strassen(sub(A12, A22), add(B21, B22))
    # Combine
    C11 = add(sub(add(M1, M4), M5), M7)
    C12 = add(M3, M5)
    C21 = add(M2, M4)
    C22 = add(sub(add(M1, M3), M2), M6)
    # Merge
    new = []
    for i in range(mid):
        new.append(C11[i] + C12[i])
    for i in range(mid):
        new.append(C21[i] + C22[i])
    return new
# Example 4x4 matrices
A = [[1,2,3,4],[5,6,7,8],[9,1,2,3],[4,5,6,7]]
B = [[7,6,5,4],[3,2,1,0],[1,2,3,4],[5,6,7,8]]

print("Naive Result:")
print(naive_multiply(A, B))

print("\nStrassen Result:")
print(strassen(A, B))

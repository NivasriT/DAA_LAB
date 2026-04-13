print("NIVASRI T | 24BAD081")# Task 2: Count Scalar Multiplications
naive_count = 0
strassen_count = 0
def naive_multiply_count(A, B):
    global naive_count
    n = len(A)
    C = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                naive_count += 1
                C[i][j] += A[i][k] * B[k][j]
    return C
def add(A, B):
    n = len(A)
    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]

def sub(A, B):
    n = len(A)
    return [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]
def strassen_count_func(A, B):
    global strassen_count
    n = len(A)
    if n == 1:
        strassen_count += 1
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

    M1 = strassen_count_func(add(A11, A22), add(B11, B22))
    M2 = strassen_count_func(add(A21, A22), B11)
    M3 = strassen_count_func(A11, sub(B12, B22))
    M4 = strassen_count_func(A22, sub(B21, B11))
    M5 = strassen_count_func(add(A11, A12), B22)
    M6 = strassen_count_func(sub(A21, A11), add(B11, B12))
    M7 = strassen_count_func(sub(A12, A22), add(B21, B22))

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
# Create 8x8 matrices
import random
n = 8
A = [[random.randint(1,5) for _ in range(n)] for _ in range(n)]
B = [[random.randint(1,5) for _ in range(n)] for _ in range(n)]
naive_multiply_count(A, B)
strassen_count_func(A, B)
print("Naive Multiplications:", naive_count)
print("Strassen Multiplications:", strassen_count)

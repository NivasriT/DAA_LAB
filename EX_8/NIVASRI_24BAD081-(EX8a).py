# Matrix Chain Multiplication (DP)
print("NIVASRI T | 24BAD081")
# Function to print optimal order
def print_order(s, i, j):
    if i == j:
        print("A"+str(i+1), end="")
    else:
        print("(", end="")
        print_order(s, i, s[i][j])
        print_order(s, s[i][j]+1, j)
        print(")", end="")

# Input: matrix dimensions
p = [10, 30, 5, 60]   # A1=10x30, A2=30x5, A3=5x60

n = len(p) - 1

# DP table
m = [[0]*n for _ in range(n)]
s = [[0]*n for _ in range(n)]

# Fill DP table
for L in range(2, n+1):
    for i in range(n-L+1):
        j = i + L - 1
        m[i][j] = 999999

        for k in range(i, j):
            cost = m[i][k] + m[k+1][j] + p[i]*p[k+1]*p[j+1]

            if cost < m[i][j]:
                m[i][j] = cost
                s[i][j] = k

# Task 3: Display DP Table
print("DP Table:")
for row in m:
    print(row)

# Task 2: Print optimal parenthesization
print("\nOptimal Parenthesization:")
print_order(s, 0, n-1)

# Task 3: Final result
print("\n\nMinimum Scalar Multiplications:", m[0][n-1])

# Task 1: Create board
print("NIVASRI T | 24BAD081")
N = 4
board = [[0]*N for _ in range(N)]

solutions = 0  # count solutions

# Check if safe to place queen
def is_safe(row, col):
    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check left diagonal
    i, j = row-1, col-1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check right diagonal
    i, j = row-1, col+1
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

# Task 2: Backtracking
def solve(row):
    global solutions

    if row == N:
        # Task 3: Print solution
        print("\nSolution", solutions+1)
        for r in board:
            print(r)
        solutions += 1
        return

    for col in range(N):
        if is_safe(row, col):
            board[row][col] = 1   # place queen
            solve(row + 1)        # next row
            board[row][col] = 0   # backtrack

# Run
solve(0)

print("\nTotal solutions:", solutions)

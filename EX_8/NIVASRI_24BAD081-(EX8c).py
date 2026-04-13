# 0/1 Knapsack Problem
print("NIVASRI T| 24BAD081")
# Input
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5
n = len(weights)
# Task 1: Bottom-Up (DP Table)
dp = [[0]*(capacity+1) for _ in range(n+1)]

for i in range(1, n+1):
    for w in range(capacity+1):
        if weights[i-1] <= w:
            dp[i][w] = max(dp[i-1][w],
                           dp[i-1][w-weights[i-1]] + values[i-1])
        else:
            dp[i][w] = dp[i-1][w]
print("DP Table:")
for row in dp:
    print(row)
# Task 2: Backtracking
w = capacity
selected = []
for i in range(n, 0, -1):
    if dp[i][w] != dp[i-1][w]:
        selected.append(i-1)
        w -= weights[i-1]

print("\nSelected Items:")
for i in selected:
    print("Item", i+1, "Weight:", weights[i], "Value:", values[i])
# Task 3: Top-Down (Memoization)
memo = [[-1]*(capacity+1) for _ in range(n+1)]
def knapsack(i, w):
    if i == 0 or w == 0:
        return 0

    if memo[i][w] != -1:
        return memo[i][w]

    if weights[i-1] <= w:
        memo[i][w] = max(knapsack(i-1, w),
                         knapsack(i-1, w-weights[i-1]) + values[i-1])
    else:
        memo[i][w] = knapsack(i-1, w)

    return memo[i][w]

max_value_topdown = knapsack(n, capacity)
# Task 4: Memo Table

print("\nMemoization Table:")
for row in memo:
    print(row)
# Task 5: Final Output
print("\nMaximum Value (Bottom-Up):", dp[n][capacity])
print("Maximum Value (Top-Down):", max_value_topdown)

# Task 1: Graph using adjacency matrix
print("NIVASRI T |24BAD081")
graph = [
    [0,1,1,0],
    [1,0,1,1],
    [1,1,0,1],
    [0,1,1,0]
]

n = len(graph)
color = [0] * n   # store colors

# Check if safe to color
def is_safe(v, c):
    for i in range(n):
        if graph[v][i] == 1 and color[i] == c:
            return False
    return True

# Task 2: Backtracking function
def solve(v, m):
    if v == n:
        return True

    for c in range(1, m+1):
        if is_safe(v, c):
            color[v] = c
            if solve(v+1, m):
                return True
            color[v] = 0   # backtrack

    return False

# Task 4: Find minimum chromatic number
for m in range(1, n+1):
    color = [0]*n
    if solve(0, m):
        print("Minimum colors needed:", m)
        break

# Task 3: Output
print("Vertex Colors:")
for i in range(n):
    print("Vertex", i, "-> Color", color[i])

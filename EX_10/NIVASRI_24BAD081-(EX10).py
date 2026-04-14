import heapq
print("NIVASRI T | 24BAD081")
# Node structure
class Node:
    def __init__(self, path, cost, bound, level):
        self.path = path        # visited cities
        self.cost = cost        # cost so far
        self.bound = bound      # lower bound
        self.level = level      # depth
    def __lt__(self, other):
        return self.bound < other.bound
# Function to calculate lower bound
def calculate_bound(cost, path, n):
    bound = 0
    visited = set(path)
    for i in range(n):
        if i not in visited:
            min_cost = float('inf')
            for j in range(n):
                if i != j:
                    min_cost = min(min_cost, cost[i][j])
            bound += min_cost
    return bound
# Branch and Bound TSP
def tsp_branch_and_bound(cost):
    n = len(cost)
    # Priority Queue
    pq = []
    # Initial node
    start = Node(path=[0], cost=0, bound=0, level=0)
    start.bound = calculate_bound(cost, start.path, n)
    heapq.heappush(pq, start)
    min_cost = float('inf')
    best_path = []
    print("Step-by-step exploration:\n")
    while pq:
        current = heapq.heappop(pq)
        print(f"Exploring path: {current.path} | Cost: {current.cost} | Bound: {current.bound}")
        # If full path found
        if current.level == n - 1:
            total_cost = current.cost + cost[current.path[-1]][0]
            if total_cost < min_cost:
                min_cost = total_cost
                best_path = current.path + [0]
            continue
        # Generate child nodes
        for i in range(n):
            if i not in current.path:
                new_path = current.path + [i]
                new_cost = current.cost + cost[current.path[-1]][i]
                new_bound = new_cost + calculate_bound(cost, new_path, n)
                # Pruning
                if new_bound < min_cost:
                    child = Node(new_path, new_cost, new_bound, current.level + 1)
                    heapq.heappush(pq, child)
    return best_path, min_cost
# Example cost matrix
cost = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
# Run TSP
path, min_cost = tsp_branch_and_bound(cost)
print("\nOptimal Tour Path:", path)
print("Minimum Tour Cost:", min_cost)

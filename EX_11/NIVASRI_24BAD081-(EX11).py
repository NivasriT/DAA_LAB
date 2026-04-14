# ---------- Task 1: Graph Representation ----------
print("NIVASRI T | 24BAD081")
# Edge list (u, v)
edges = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4)]

# Number of vertices
n = 5

# ---------- Utility Function ----------
def is_covered(edges, cover):
    for u, v in edges:
        if u not in cover and v not in cover:
            return False
    return True

# ---------- Task 2: 2-Approximation Algorithm ----------
def vertex_cover_approx(edges):
    edges_left = edges.copy()
    cover = set()

    print("\n2-Approximation Steps:")

    while edges_left:
        # Pick any edge
        u, v = edges_left[0]
        print(f"Pick edge ({u}, {v}) → add {u}, {v}")

        # Add both vertices
        cover.add(u)
        cover.add(v)

        # Remove all edges connected to u or v
        new_edges = []
        for x, y in edges_left:
            if x != u and x != v and y != u and y != v:
                new_edges.append((x, y))

        edges_left = new_edges

    return cover

# ---------- Task 3: Greedy Degree-Based Algorithm ----------
def vertex_cover_greedy(edges, n):
    edges_left = edges.copy()
    cover = set()

    print("\nGreedy Steps:")

    while edges_left:
        # Calculate degree
        degree = [0] * n
        for u, v in edges_left:
            degree[u] += 1
            degree[v] += 1

        # Pick vertex with max degree
        max_deg = max(degree)
        vertex = degree.index(max_deg)

        print(f"Pick vertex {vertex} with degree {max_deg}")

        cover.add(vertex)

        # Remove all edges connected to this vertex
        new_edges = []
        for u, v in edges_left:
            if u != vertex and v != vertex:
                new_edges.append((u, v))

        edges_left = new_edges

    return cover


# ---------- Run Both Algorithms ----------

approx_cover = vertex_cover_approx(edges)
greedy_cover = vertex_cover_greedy(edges, n)


# ---------- Task 4: Output ----------

print("\n--- Final Results ---")

print("\n2-Approximation Vertex Cover:", approx_cover)
print("Total vertices:", len(approx_cover))
print("All edges covered:", is_covered(edges, approx_cover))

print("\nGreedy Vertex Cover:", greedy_cover)
print("Total vertices:", len(greedy_cover))
print("All edges covered:", is_covered(edges, greedy_cover))

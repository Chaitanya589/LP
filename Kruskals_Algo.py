# Function to find the parent of a node
def find_parent(parent, node):
    if parent[node] != node:
        parent[node] = find_parent(parent, parent[node])
    return parent[node]

# Function to perform union of two sets
def union(parent, u, v):
    root_u = find_parent(parent, u)
    root_v = find_parent(parent, v)
    if root_u != root_v:
        parent[root_v] = root_u

# Kruskal's Algorithm
def kruskal(vertices, edges):
    # Step 1: Sort edges by weight
    edges.sort(key=lambda x: x[2])  # (u, v, weight)

    # Step 2: Initialize parent for each vertex
    parent = {v: v for v in vertices}
    mst = []

    # Step 3: Pick edges
    for u, v, weight in edges:
        if find_parent(parent, u) != find_parent(parent, v):
            mst.append((u, v, weight))
            union(parent, u, v)

    return mst

# Example Graph
vertices = ['A', 'B', 'C', 'D']
edges = [
    ('A', 'B', 1),
    ('A', 'C', 3),
    ('B', 'D', 4),
    ('C', 'D', 2)
]

# Run Kruskal's Algorithm
mst = kruskal(vertices, edges)

# Print Result
print("Minimum Spanning Tree:")
for u, v, weight in mst:
    print(f"{u} -- {v} == {weight}")

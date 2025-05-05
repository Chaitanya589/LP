
G = [
    [0, 1, 1, 0, 1, 0],
    [1, 0, 1, 1, 0, 1],
    [1, 1, 0, 1, 1, 0],
    [0, 1, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 1],
    [0, 1, 0, 1, 1, 0]
]

nodes = "abcdef"

# Map node names to indices
node_index = {nodes[i]: i for i in range(len(G))}

# Calculate degree of each node
degree = [sum(G[i]) for i in range(len(G))]

# Available colors
colors = ["Blue", "Red", "Yellow", "Green"]

# Assign initial full color list to each node
colorDict = {node: colors.copy() for node in nodes}

# Sort nodes by descending degree
sortedNode = []
used_indices = []
for _ in range(len(degree)):
    max_deg = -1
    idx = -1
    for j in range(len(degree)):
        if j not in used_indices and degree[j] > max_deg:
            max_deg = degree[j]
            idx = j
    used_indices.append(idx)
    sortedNode.append(nodes[idx])

# Assign colors using greedy algorithm
theSolution = {}
for n in sortedNode:
    current_color = colorDict[n][0]  # Pick the first available color
    theSolution[n] = current_color

    # Remove this color from adjacent nodes
    for j in range(len(G[node_index[n]])):
        if G[node_index[n]][j] == 1:
            neighbor = nodes[j]
            if current_color in colorDict[neighbor]:
                colorDict[neighbor].remove(current_color)

# Output result
print("Node Coloring Result:")
for t in sorted(theSolution):
    print("Node", t, "=", theSolution[t])

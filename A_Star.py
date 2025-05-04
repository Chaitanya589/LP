import heapq

def a_star(start, goal, graph, heuristic):
    open_set = [(0 + heuristic[start], 0, start, [start])]  # (f, g, node, path)
    visited = set()

    while open_set:
        f, g, node, path = heapq.heappop(open_set)
        if node == goal:
            return path

        if node in visited:
            continue
        visited.add(node)

        for neighbor, cost in graph.get(node, []):
            if neighbor in visited:
                continue
            new_g = g + cost
            new_f = new_g + heuristic.get(neighbor, float('inf'))
            heapq.heappush(open_set, (new_f, new_g, neighbor, path + [neighbor]))

    return None  # No path found

# Graph representation
graph = {
    'A': [('B', 2), ('E', 3)],
    'B': [('A', 2), ('C', 1), ('G', 9)],
    'C': [('B', 1)],
    'D': [('E', 6), ('G', 1)],
    'E': [('A', 3), ('D', 6)],
    'G': [('B', 9), ('D', 1)]
}

# Heuristic values (straight-line estimate to goal)
heuristic = {
    'A': 4,
    'B': 2,
    'C': 6,
    'D': 1,
    'E': 5,
    'G': 0
}

# Run
path = a_star('A', 'G', graph, heuristic)
if path:
    print("Path found:", path)
else:
    print("No path found.")

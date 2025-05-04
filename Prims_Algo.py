import heapq

def prim(graph):
    mst = []
    visited = set()
    min_heap = [(0, 'A')]  # (weight, node)
    
    while min_heap:
        weight, node = heapq.heappop(min_heap)
        if node not in visited:
            visited.add(node)
            mst.append((node, weight))
            for neighbor, edge_weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (edge_weight, neighbor))
    
    return mst

# Example usage:
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

mst = prim(graph)
print("Minimum Spanning Tree:", mst)

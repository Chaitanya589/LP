import heapq

def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    min_heap = [(0, start)]  # (distance, node)
    
    while min_heap:
        current_dist, node = heapq.heappop(min_heap)
        if current_dist > dist[node]:
            continue
        for neighbor, weight in graph[node]:
            distance = current_dist + weight
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(min_heap, (distance, neighbor))
    
    return dist

# Example usage:
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

distances = dijkstra(graph, 'A')
print("Shortest distances from A:", distances)

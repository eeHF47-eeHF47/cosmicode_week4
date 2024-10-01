# Task 5: Write a program to find the shortest path in a graph using Dijkstra's algorithm.
def dijkstra(graph, start):
    # Dictionary to store the shortest distances from the start node
    shortest_distances = {node: float('inf') for node in graph}
    shortest_distances[start] = 0

    visited = []

    while len(visited) < len(graph):
        # Find the unvisited node with the smallest distance
        min_distance_node = None
        for node in graph:
            if node not in visited:
                if min_distance_node is None:
                    min_distance_node = node
                elif shortest_distances[node] < shortest_distances[min_distance_node]:
                    min_distance_node = node

        # Get the current shortest distance
        current_distance = shortest_distances[min_distance_node]

        # Check neighbors and update their distances
        for neighbor, weight in graph[min_distance_node]:
            if neighbor not in visited:
                new_distance = current_distance + weight
                if new_distance < shortest_distances[neighbor]:
                    shortest_distances[neighbor] = new_distance

        # Mark the current node as visited
        visited.append(min_distance_node)

    return shortest_distances

# Example graph as an adjacency list
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

start_node = 'A'
shortest_distances = dijkstra(graph, start_node)

print("Shortest distances from node", start_node)
for node, distance in shortest_distances.items():
    print(f"To {node}: {distance}")

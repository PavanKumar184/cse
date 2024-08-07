def dijkstra(graph, start_vertex):
    num_vertices = len(graph)
    distances = {vertex: float('inf') for vertex in range(num_vertices)}
    previous_vertices = {vertex: None for vertex in range(num_vertices)}
    distances[start_vertex] = 0
    visited = [False] * num_vertices

    for _ in range(num_vertices):
        # Find the vertex with the minimum distance from the set of vertices not yet processed
        min_distance = float('inf')
        min_vertex = -1
        for vertex in range(num_vertices):
            if not visited[vertex] and distances[vertex] < min_distance:
                min_distance = distances[vertex]
                min_vertex = vertex

        # Mark the chosen vertex as processed
        visited[min_vertex] = True

        # Update the distance value of the adjacent vertices of the chosen vertex
        for neighbor, weight in graph[min_vertex].items():
            if not visited[neighbor] and distances[min_vertex] + weight < distances[neighbor]:
                distances[neighbor] = distances[min_vertex] + weight
                previous_vertices[neighbor] = min_vertex

    return distances, previous_vertices

def print_path(previous_vertices, vertex):
    path = []
    while vertex is not None:
        path.insert(0, vertex)
        vertex = previous_vertices[vertex]
    return path

# User input for number of vertices
num_vertices = int(input("Enter the number of vertices: "))

# Initialize the graph
graph = {i: {} for i in range(num_vertices)}

# User input for number of edges
num_edges = int(input("Enter the number of edges: "))

# Input the edges and weights
print("Enter the edges in the format: u v w (where u is the start vertex, v is the end vertex, and w is the weight):")
for _ in range(num_edges):
    u, v, w = map(int, input().split())
    graph[u][v] = w

# Input the source vertex
source_vertex = int(input("Enter the source vertex: "))

# Calculate shortest paths using Dijkstra's algorithm
distances, previous_vertices = dijkstra(graph, source_vertex)

# Print the result
print("Vertex Distance from Source")
for vertex in range(num_vertices):
    print(f"{vertex}\t\t{distances[vertex]}")

# Print the paths from the source to each vertex
print("\nPaths from the source vertex:")
for vertex in range(num_vertices):
    path = print_path(previous_vertices, vertex)
    print(f"Path to vertex {vertex}: {' -> '.join(map(str, path))}")

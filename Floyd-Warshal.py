def floyd_warshall(graph):
    """
    Finds the shortest distances between every pair of vertices in a weighted graph.
    'float("inf")' represents no direct edge between two vertices.
    """
    num_vertices = len(graph)
    
    # Create a copy of the graph to store shortest distances
    dist = [row[:] for row in graph]

    # Iterate through each vertex as an intermediate point (k)
    for k in range(num_vertices):
        # Pick all vertices as source (i)
        for i in range(num_vertices):
            # Pick all vertices as destination (j)
            for j in range(num_vertices):
                # Update dist[i][j] if vertex k offers a shorter path
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

# Example Usage
if __name__ == "__main__":
    INF = float('inf')

    # Adjacency matrix representation of a 4-vertex directed graph
    graph = [
        [0,   3,   INF, 7],
        [8,   0,   2,   INF],
        [5,   INF, 0,   1],
        [2,   INF, INF, 0]
    ]

    shortest_paths = floyd_warshall(graph)

    print("Shortest distance matrix:")
    for row in shortest_paths:
        print([val if val != INF else "INF" for val in row])

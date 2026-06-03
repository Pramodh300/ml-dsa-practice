#Adjacency Matrix
# Number of nodes
n = 4

# Create empty 4x4 matrix
matrix = [[0] * n for _ in range(n)]

# Edges
edges = [
    (0,1),
    (0,2),
    (1,3),
    (2,3)
]

# Add connections
for u, v in edges:

    matrix[u][v] = 1
    matrix[v][u] = 1


# Print matrix
for row in matrix:
    print(row)


#Adjacency List
# Graph using adjacency list

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

# Print graph
print(graph)



#Add New Edge# Initial graph
graph = {
    'A': ['B'],
    'B': ['A'],
    'C': []
}

# Add edge A ---- C

graph['A'].append('C')

graph['C'].append('A')

# Print updated graph
print(graph)



#Count Connections
# Graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['B']
}

# Count neighbors
for node in graph:

    connections = len(graph[node])

    print(node, "has", connections, "connections")
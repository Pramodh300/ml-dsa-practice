#Basic DFS Traversal
# Graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': [],
    'D': [],
    'E': []
}

visited = set()

# DFS Function
def dfs(node):

    if node not in visited:

        print(node, end=" ")

        visited.add(node)

        for neighbor in graph[node]:

            dfs(neighbor)

# Run DFS
dfs('A')


#DFS with visited tracking
# Graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': [],
    'D': [],
    'E': []
}

visited = set()

# DFS Function
def dfs(node):

    if node not in visited:

        print("\nVisiting:", node)

        visited.add(node)

        print("Visited =", visited)

        for neighbor in graph[node]:

            dfs(neighbor)

# Run DFS
dfs('A')


#DFS on number graph
# Graph
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6],
    4: [],
    5: [],
    6: []
}

visited = set()

# DFS Function
def dfs(node):

    if node not in visited:

        print(node, end=" ")

        visited.add(node)

        for neighbor in graph[node]:

            dfs(neighbor)

# Run DFS
dfs(1)


#Find reachable nodes
# Graph
graph = {
    'A': ['B'],
    'B': ['A', 'C'],
    'C': ['B'],
    'D': []
}

visited = set()

# DFS Function
def dfs(node):

    if node not in visited:

        print(node, end=" ")

        visited.add(node)

        for neighbor in graph[node]:

            dfs(neighbor)

# Start DFS from A
dfs('A')
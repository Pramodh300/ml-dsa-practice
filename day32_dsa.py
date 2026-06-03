#Basic BFS Traversal
from collections import deque

# Graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': [],
    'D': [],
    'E': []
}

# BFS Function
def bfs(graph, start):

    visited = set()

    queue = deque([start])

    while queue:

        node = queue.popleft()

        if node not in visited:

            print(node, end=" ")

            visited.add(node)

            queue.extend(graph[node])


# Run BFS
bfs(graph, 'A')


#Trace Queue Manually
from collections import deque

# Graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': [],
    'D': [],
    'E': []
}

# BFS Function
def bfs(graph, start):

    visited = set()

    queue = deque([start])

    while queue:

        print("\nQueue:", list(queue))

        node = queue.popleft()

        if node not in visited:

            print("Visit:", node)

            visited.add(node)

            print("Visited Nodes:", visited)

            queue.extend(graph[node])


# Run BFS
bfs(graph, 'A')



#BFS on Number Graph
from collections import deque

# Graph
graph = {
    1: [2,3],
    2: [4,5],
    3: [6],
    4: [],
    5: [],
    6: []
}

# BFS Function
def bfs(graph, start):

    visited = set()

    queue = deque([start])

    while queue:

        node = queue.popleft()

        if node not in visited:

            print(node, end=" ")

            visited.add(node)

            queue.extend(graph[node])


# Run BFS
bfs(graph, 1)



#Find Connected Nodes
from collections import deque

# Graph
graph = {
    'A': ['B'],
    'B': ['A', 'C'],
    'C': ['B'],
    'D': []
}

# BFS Function
def bfs(graph, start):

    visited = set()

    queue = deque([start])

    while queue:

        node = queue.popleft()

        if node not in visited:

            print(node, end=" ")

            visited.add(node)

            queue.extend(graph[node])


# Run BFS
bfs(graph, 'A')


#Instagram Friend Network BFS
from collections import deque

# Instagram Friend Network
graph = {
    'You': ['A', 'B'],
    'A': ['C'],
    'B': ['D'],
    'C': [],
    'D': []
}

# BFS Function
def bfs(graph, start):

    visited = set()

    queue = deque([start])

    while queue:

        node = queue.popleft()

        if node not in visited:

            print(node, end=" ")

            visited.add(node)

            queue.extend(graph[node])


# Run BFS
bfs(graph, 'You')
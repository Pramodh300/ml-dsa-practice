#Queue -> BSE
from collections import deque

graph = {
    1: [2, 3],
    2: [4, 5],
    3: [],
    4: [],
    5: []
}

def bfs(graph, start):
    queue = deque()
    visited = set()

    queue.append(start)
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

bfs(graph, 2)
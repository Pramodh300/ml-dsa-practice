#Count Connected Components
graph = {
    'A': ['B'],
    'B': ['A', 'C'],
    'C': ['B'],
    'D': ['E'],
    'E': ['D'],
    'F': []
}

visited = set()

def dfs(node):

    visited.add(node)

    print(node, end=" ")

    for neighbor in graph[node]:

        if neighbor not in visited:

            dfs(neighbor)

components = 0

for node in graph:

    if node not in visited:

        components += 1

        print(f"\nComponent {components}:", end=" ")

        dfs(node)

print("\n")
print("Total Components:", components)



#Number of Islands
grid = [
    [1,1,0,0],
    [1,0,0,1],
    [0,0,1,1],
    [0,0,0,1]
]

rows = len(grid)
cols = len(grid[0])

def dfs(r, c):

    if (
        r < 0 or
        c < 0 or
        r >= rows or
        c >= cols or
        grid[r][c] == 0
    ):
        return

    grid[r][c] = 0

    dfs(r+1, c)
    dfs(r-1, c)
    dfs(r, c+1)
    dfs(r, c-1)

islands = 0

for r in range(rows):

    for c in range(cols):

        if grid[r][c] == 1:

            islands += 1

            dfs(r, c)

print("Number of Islands:", islands)



#Largest Island Size
grid = [
    [1,1,0,0],
    [1,1,0,1],
    [0,0,1,1],
    [0,0,0,1]
]

rows = len(grid)
cols = len(grid[0])

def dfs(r, c):

    if (
        r < 0 or
        c < 0 or
        r >= rows or
        c >= cols or
        grid[r][c] == 0
    ):
        return 0

    grid[r][c] = 0

    size = 1

    size += dfs(r+1, c)
    size += dfs(r-1, c)
    size += dfs(r, c+1)
    size += dfs(r, c-1)

    return size

largest = 0

for r in range(rows):

    for c in range(cols):

        if grid[r][c] == 1:

            current_size = dfs(r, c)

            largest = max(
                largest,
                current_size
            )

print("Largest Island Size:", largest)
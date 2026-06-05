#Detect Cycle
graph = {
    'A': ['B'],
    'B': ['C'],
    'C': ['A']
}

visited = set()
rec_stack = set()

def has_cycle(node):

    visited.add(node)
    rec_stack.add(node)

    for neighbor in graph[node]:

        if neighbor not in visited:

            if has_cycle(neighbor):
                return True

        elif neighbor in rec_stack:
            return True

    rec_stack.remove(node)

    return False


if has_cycle('A'):
    print("Cycle Found")
else:
    print("No Cycle")



#No cycle
graph = {
    'A': ['B'],
    'B': ['C'],
    'C': []
}

visited = set()
rec_stack = set()

def has_cycle(node):

    visited.add(node)
    rec_stack.add(node)

    for neighbor in graph[node]:

        if neighbor not in visited:

            if has_cycle(neighbor):
                return True

        elif neighbor in rec_stack:
            return True

    rec_stack.remove(node)

    return False


if has_cycle('A'):
    print("Cycle Found")
else:
    print("No Cycle")



#Print Visited and Recursion Stack
graph = {
    'A': ['B'],
    'B': ['C'],
    'C': ['A']
}

visited = set()
rec_stack = set()

def has_cycle(node):

    visited.add(node)
    rec_stack.add(node)

    print("\nVisited:", visited)
    print("Rec Stack:", rec_stack)

    for neighbor in graph[node]:

        if neighbor not in visited:

            if has_cycle(neighbor):
                return True

        elif neighbor in rec_stack:

            print("\nCycle Found at:", neighbor)

            return True

    rec_stack.remove(node)

    return False


if has_cycle('A'):
    print("\nCycle Detected")
else:
    print("\nNo Cycle")


#Number Graph Cycle Detection
graph = {
    1: [2],
    2: [3],
    3: [1]
}

visited = set()
rec_stack = set()

def has_cycle(node):

    visited.add(node)
    rec_stack.add(node)

    for neighbor in graph[node]:

        if neighbor not in visited:

            if has_cycle(neighbor):
                return True

        elif neighbor in rec_stack:
            return True

    rec_stack.remove(node)

    return False


print(has_cycle(1))



#Disconnected Graph
graph = {
    'A': ['B'],
    'B': [],
    'C': ['D'],
    'D': ['C']
}

visited = set()
rec_stack = set()

def has_cycle(node):

    visited.add(node)
    rec_stack.add(node)

    for neighbor in graph[node]:

        if neighbor not in visited:

            if has_cycle(neighbor):
                return True

        elif neighbor in rec_stack:
            return True

    rec_stack.remove(node)

    return False


cycle_found = False

for node in graph:

    if node not in visited:

        if has_cycle(node):
            cycle_found = True
            break


if cycle_found:
    print("Cycle Found")
else:
    print("No Cycle")
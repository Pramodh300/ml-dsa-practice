#Height of tree
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Build tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

def Height(root):
    if root is None:
        return 0
    left = Height(root.left)
    right = Height(root.right)

    return 1 + max(left, right)

print(Height(root))


#Diameter of Tree
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Build tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

def Height(root):
    if root is None:
        return 0
    left = Height(root.left)
    right = Height(root.right)

    return 1 + max(left, right)

def diameter(root):
    if root is None:
        return 0
    left = Height(root.left)
    right = Height(root.right)

    left_diameter = diameter(root.left)
    right_diameter = diameter(root.right)

    return max(left + right + 1,
               left_diameter,
               right_diameter
    )
print("Diameter: ",diameter(root))


#Diameter of Tree
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Build tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(6)

def Height(root):
    if root is None:
        return 0
    left = Height(root.left)
    right = Height(root.right)

    return 1 + max(left, right)

def diameter(root):
    if root is None:
        return 0
    left = Height(root.left)
    right = Height(root.right)

    left_diameter = diameter(root.left)
    right_diameter = diameter(root.right)

    return max(left + right + 1,
               left_diameter,
               right_diameter
    )
print("Diameter: ",diameter(root))
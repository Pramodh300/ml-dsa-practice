#Binary tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, arr):
        if not arr:
            return None
        
        self.root = Node(arr[0])
        queue = [self.root]
        i = 1

        while queue and i < len(arr):
            node = queue.pop(0)

            if i < len(arr) and arr[i] is not None:
                node.left = Node(arr[i])
                queue.append(node.left)

            i += 1

            if i < len(arr) and arr[i] is not None:
                node.right = Node(arr[i])
                queue.append(node.right)

            i += 1

        return self.root
    
    #Inorder
    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.left)
        print(node.data, end=' ')
        self.inorder(node.right)


    #Level order
    def level_order(self, node):
        if node is None:
            return
        
        queue = [node]
        while queue:
            current = queue.pop(0)
            print(current.data, end=' ')
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

bt = BinaryTree()
arr = [1, 2, 3, 4, 5, 6, 7]
bt.insert(arr)
bt.inorder(bt.root)
print("\n")
bt.level_order(bt.root)
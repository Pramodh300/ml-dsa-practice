class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Binaray_tree:
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
    
    #inorder()
    def inorder(self, node):
        if node is None:
            return
        
        self.inorder(node.left)
        print(node.data, end=' ')
        self.inorder(node.right)


    #preorder
    def preorder(self, node):
        if node is None:
            return
        
        print(node.data)
        self.preorder(node.left)
        self.preorder(node.right)

    #postorder
    def postorder(self, node):
        if node is None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.data)

bt = Binaray_tree()
arr = [1, 2, 3, 4, 5]
bt.insert(arr)
bt.inorder(bt.root)
print("\n")
bt.preorder(bt.root)
print("\n")
bt.postorder(bt.root)
#Insert
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    #Insert
    
    def insert(self, val):
        if not self.root:
            self.root = Node(val)

        else:
            self._insert(self.root, val)

    
    def _insert(self, node, val):
        if val < node.val:
            if node.left is None:
                node.left = Node(val)

            else:
                self._insert(node.left, val)

        else:
            if node.right is None:
                node.right = Node(val)

            else:
                self._insert(node.right, val)

    #Search

    def search(self, val):
        return self._search(self.root, val)
    
    def _search(self, node, val):
        if node is None:
            return False
        if node.val == val:
            return True
        elif val < node.val:
            return self._search(node.left, val)
        else:
            return self._search(node.right, val)
    
    #Valid
    def is_valid_bst(self):
        return self._validate(self.root, float('-inf'), float('inf'))

    def _validate(self, node, min_val, max_val):
        if node is None:
            return True
        if not (min_val < node.val < max_val):
            return False
        return (self._validate(node.left,  min_val,   node.val) and
                self._validate(node.right, node.val,  max_val))
    

    #Inorder
    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result
    
    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.val)
            self._inorder(node.right, result)

bst = BST()
for val in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
    bst.insert(val)

print("\nSearch 6:", bst.search(6))
print("Search 5:", bst.search(5))

print("\nSearch 6:", bst.search(6))
print("Search 5:", bst.search(5))

print("Inorder: ",bst.inorder())
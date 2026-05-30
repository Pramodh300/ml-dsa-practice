#I just copied the code.
from collections import deque


# ── Tree Node Definition (shared by all problems) ──────────────────────────
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ══════════════════════════════════════════════════════════════════════════════
# 102. Binary Tree Level Order Traversal
# https://leetcode.com/problems/binary-tree-level-order-traversal/
# Difficulty: Medium
#
# Problem:
#   Given the root of a binary tree, return the level order traversal
#   of its nodes' values as a list of lists (level by level, left to right).
#
# Example:
#       3
#      / \
#     9  20
#        / \
#       15   7
#
#   Output: [[3], [9, 20], [15, 7]]
#
# Approach: BFS with a queue. At each level, record len(queue) so we
#           know exactly how many nodes belong to that level.
# Time:  O(n) — every node visited once
# Space: O(n) — queue holds at most one full level
# ══════════════════════════════════════════════════════════════════════════════
def levelOrder(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)   # nodes at current level
        level = []

        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level)

    return result


# ── Test 102 ────────────────────────────────────────────────────────────────
root102 = TreeNode(3)
root102.left = TreeNode(9)
root102.right = TreeNode(20)
root102.right.left = TreeNode(15)
root102.right.right = TreeNode(7)

print("102 Output:", levelOrder(root102))
# Expected: [[3], [9, 20], [15, 7]]


# ══════════════════════════════════════════════════════════════════════════════
# 107. Binary Tree Level Order Traversal II
# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
# Difficulty: Medium
#
# Problem:
#   Same as 102 but return levels from BOTTOM to TOP.
#
# Example:
#       3
#      / \
#     9  20
#        / \
#       15   7
#
#   Output: [[15, 7], [9, 20], [3]]
#
# Approach: Exactly like 102, but reverse the result at the end.
#           Or use appendleft() on a deque to build bottom-up directly.
# Time:  O(n)
# Space: O(n)
# ══════════════════════════════════════════════════════════════════════════════
def levelOrderBottom(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        level = []

        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level)

    return result[::-1]   # ← only difference from 102!


# ── Test 107 ────────────────────────────────────────────────────────────────
root107 = TreeNode(3)
root107.left = TreeNode(9)
root107.right = TreeNode(20)
root107.right.left = TreeNode(15)
root107.right.right = TreeNode(7)

print("107 Output:", levelOrderBottom(root107))
# Expected: [[15, 7], [9, 20], [3]]


# ══════════════════════════════════════════════════════════════════════════════
# 111. Minimum Depth of Binary Tree
# https://leetcode.com/problems/minimum-depth-of-binary-tree/
# Difficulty: Easy
#
# Problem:
#   Find the minimum depth — shortest path from root to any LEAF node.
#   A leaf is a node with NO children.
#
# Example 1:
#       3
#      / \
#     9  20
#        / \
#       15   7
#   Output: 2  (path: 3 → 9)
#
# Example 2:
#       2
#        \
#         3
#          \
#           4
#   Output: 3  (only one path: 2 → 3 → 4)
#
# Approach: BFS — the FIRST leaf node we encounter is at minimum depth.
#           Return immediately when we find it (no need to scan whole tree).
#           ⚠️ DFS works too but BFS is more efficient here since it stops early.
#
# Key trap: A node with only ONE child is NOT a leaf — don't stop there!
#
# Time:  O(n) worst case, but stops early on balanced trees
# Space: O(n)
# ══════════════════════════════════════════════════════════════════════════════
def minDepth(root):
    if not root:
        return 0

    queue = deque([(root, 1)])   # (node, depth)

    while queue:
        node, depth = queue.popleft()

        # leaf node → both children are None
        if not node.left and not node.right:
            return depth         # first leaf found = minimum depth ✅

        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))


# ── Test 111 ────────────────────────────────────────────────────────────────
root111a = TreeNode(3)
root111a.left = TreeNode(9)
root111a.right = TreeNode(20)
root111a.right.left = TreeNode(15)
root111a.right.right = TreeNode(7)
print("111 Output (balanced):", minDepth(root111a))   # Expected: 2

root111b = TreeNode(2)
root111b.right = TreeNode(3)
root111b.right.right = TreeNode(4)
print("111 Output (skewed):  ", minDepth(root111b))   # Expected: 3


# ══════════════════════════════════════════════════════════════════════════════
# 116. Populating Next Right Pointers in Each Node
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
# Difficulty: Medium
#
# Problem:
#   Each node has an extra `next` pointer (initially None).
#   Connect each node to its next RIGHT neighbor at the same level.
#   The last node at each level points to None.
#
# Example:
#        1                      1 → None
#       / \           →        / \
#      2   3                  2 → 3 → None
#     / \ / \                / \ / \
#    4  5 6  7              4→ 5→ 6→ 7 → None
#
# Approach: BFS level by level. Within each level, connect node[i].next
#           to node[i+1]. Last node in level stays None.
# Time:  O(n)
# Space: O(n)  (follow-up: O(1) using the next pointers themselves)
# ══════════════════════════════════════════════════════════════════════════════
class Node116:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next   # ← extra pointer

def connect(root):
    if not root:
        return root

    queue = deque([root])

    while queue:
        level_size = len(queue)

        for i in range(level_size):
            node = queue.popleft()

            # connect to next node ONLY if not the last in this level
            if i < level_size - 1:
                node.next = queue[0]   # peek at front of queue
            # last node's next stays None automatically

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return root


# ── Test 116 ────────────────────────────────────────────────────────────────
root116 = Node116(1)
root116.left = Node116(2)
root116.right = Node116(3)
root116.left.left = Node116(4)
root116.left.right = Node116(5)
root116.right.left = Node116(6)
root116.right.right = Node116(7)

connect(root116)

# Print next pointers level by level
node = root116
while node:
    cur = node
    row = []
    while cur:
        row.append(str(cur.val))
        cur = cur.next
    row.append("None")
    print(" -> ".join(row))
    node = node.left

# Expected:
# 1 -> None
# 2 -> 3 -> None
# 4 -> 5 -> 6 -> 7 -> None
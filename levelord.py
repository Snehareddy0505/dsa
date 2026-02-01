from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root):
    if not root:
        return

    q = deque([root])

    while q:
        node = q.popleft()
        print(node.val, end=" ")

        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
# Tree:
#     1
#    / \
#   2   3

root = TreeNode(1, TreeNode(2), TreeNode(3))
levelOrder(root)

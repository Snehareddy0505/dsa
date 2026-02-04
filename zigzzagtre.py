class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque

def zigzagTraversal(root):
    if root is None:
        return []

    result = []
    q = deque([root])
    left_to_right = True

    while q:
        level_size = len(q)
        level = deque()

        for _ in range(level_size):
            node = q.popleft()

            if left_to_right:
                level.append(node.val)
            else:
                level.appendleft(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        result.append(list(level))
        left_to_right = not left_to_right

    return result
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
ans = zigzagTraversal(root)
print(ans)

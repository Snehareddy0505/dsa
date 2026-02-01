class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def maxdepth(root):
    if root is None:
        return 0

    lh = maxdepth(root.left)
    rh = maxdepth(root.right)

    return 1 + max(lh, rh)
# Tree:
#     1
#    / \
#   2   3
#      /
#     4

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)

print(maxdepth(root))  # Output: 3

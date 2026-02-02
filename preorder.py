class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorder(root):
    if not root:
        return
    print(root.val, end=" ")
    preorder(root.left)
    preorder(root.right)
# Tree:
#     1
#    / \
#   2   3

root = TreeNode(1, TreeNode(2), TreeNode(3))
preorder(root)

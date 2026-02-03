class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rightorleft(node, level):
    if node is None:
        return
    if level == len(ds):
        ds.append(node.val)
    rightorleft(node.right, level + 1)
    rightorleft(node.left, level + 1)

# build tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.right.right = TreeNode(4)

ds = []
rightorleft(root, 0)

print(ds)

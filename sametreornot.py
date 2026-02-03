class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sametreeornot(p, q):
    if p is None and q is None:
        return True

    if p is None or q is None:
        return False

    return (
        p.val == q.val and
        sametreeornot(p.left, q.left) and
        sametreeornot(p.right, q.right)
    )
t1 = TreeNode(1, TreeNode(2), TreeNode(3))
t2 = TreeNode(1, TreeNode(2), TreeNode(3))

print(sametreeornot(t1, t2))   # True

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        self.first = None
        self.middle = None
        self.last = None
        self.prev = TreeNode(float('-inf'))

        def inorder(node):
            if not node:
                return
            inorder(node.left)

            # Detect violation
            if self.prev.val > node.val:
                if not self.first:
                    self.first = self.prev
                    self.middle = node
                else:
                    self.last = node

            self.prev = node
            inorder(node.right)

        inorder(root)

        # Fix swapped nodes
        if self.first and self.last:
            self.first.val, self.last.val = self.last.val, self.first.val
        elif self.first and self.middle:
            self.first.val, self.middle.val = self.middle.val, self.first.val
root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(2)
def inorder_print(root):
    if not root:
        return
    inorder_print(root.left)
    print(root.val, end=" ")
    inorder_print(root.right)
print("Before recovery:")
inorder_print(root)    # Wrong order
print()

Solution().recoverTree(root)

print("After recovery:")
inorder_print(root)    # Correct order

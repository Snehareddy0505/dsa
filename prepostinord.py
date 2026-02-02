# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def allTraversals(self, root):
        preorder = []
        inorder = []
        postorder = []

        def dfs(node):
            if not node:
                return

            # Preorder
            preorder.append(node.val)

            dfs(node.left)

            # Inorder
            inorder.append(node.val)

            dfs(node.right)

            # Postorder
            postorder.append(node.val)

        dfs(root)
        return preorder, inorder, postorder


# Example usage:
# Tree:
#     1
#      \
#       2
#      /
#     3

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

sol = Solution()
pre, ino, post = sol.allTraversals(root)

print("Preorder:", pre)
print("Inorder:", ino)
print("Postorder:", post)

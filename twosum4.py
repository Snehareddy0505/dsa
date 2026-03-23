class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        seen = set()

        def dfs(node):
            if not node:
                return False

            if (k - node.val) in seen:
                return True

            seen.add(node.val)
            return dfs(node.left) or dfs(node.right)

        return dfs(root)
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)

sol = Solution()
print(sol.findTarget(root, 9))   # True (2 + 7)
print(sol.findTarget(root, 28))  # False

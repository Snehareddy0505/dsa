from collections import deque, defaultdict
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root):
        if not root:
            return []

        q = deque([(root, 0, 0)])  # (node, vertical, level)
        d = defaultdict(lambda: defaultdict(list))

        while len(q) > 0:
            node, vertical, level = q.popleft()
            d[vertical][level].append(node.val)

            if node.left:
                q.append((node.left, vertical - 1, level + 1))
            if node.right:
                q.append((node.right, vertical + 1, level + 1))

        ans = []
        for i in sorted(d.keys()):
            col = []
            for j in sorted(d[i].keys()):
                col.extend(sorted(d[i][j]))
            ans.append(col)
        return ans
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
sol = Solution()
result = sol.verticalTraversal(root)
print(result)

